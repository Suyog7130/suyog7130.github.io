---
title: "Making PyTorch model training super-fast on cuda"
date: 2026-06-19
tags:
    - cuda
    - ml
    - pytorch
---

**DISCLAIMER:** Made with Google Gemini-Pro prompts.

I restructured all my `Python` installation in the system and have now committed to use only Anaconda `conda` environments to manage my Pythons. Below are some steps I followed to clean my directories!

<!--# Unbreaking PyTorch Data Pipelines: From 35-Minute Stalls to 3-Minute Epochs-->

*A deep dive into fixing OpenMP runtime conflicts, eliminating TorchDynamo graph breaks, and breaking the silent HDF5 global process lock for Gravitational-Wave VAE models.*

---

## The Starting Point: An Absolute Stall

When training heavy gravitational-wave parameter estimation and population models (utilizing libraries like `bilby` and `gwpopulation`), we hit a wall. On high-end institutional cluster hardware (NVIDIA A100-SXM4-80GB) and modern local Apple Silicon architectures (MPS), a single training epoch was taking upwards of **35 minutes**. 

Worse yet, attempts to use `torch.compile()` were failing, throwing massive Triton shared memory errors, runtime warnings, and experiencing zero epoch-to-epoch speed improvements.

By systematically hunting down **runtime conflicts**, **compiler graph breaks**, and a **silent I/O bottleneck**, we slashed training times from **35 minutes down to an incredible 3 minutes per epoch**. 

Here is exactly how we did it.

---

## Step 1: Resolving the Multiprocessing Runtime Conflict
The very first hurdle was an OpenMP crash preventing clean environment execution:

```text
OMP: Error #15: Initializing libomp.dylib, but found libomp.dylib already initialized.
```

**The Cause:** PyTorch and underlying linear algebra libraries (like MKL/OpenBLAS via NumPy) each loaded their own isolated copies of the OpenMP runtime into memory simultaneously.

**The Fix:** Force the Conda environment to use a single, unified OpenMP implementation:

```bash
conda install -c conda-forge nomkl
# Or fallback directly in code if needed for quick cluster testing:
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
```

---

## Step 2: Decoding the "Greedy" Triton Compiler Errors

When trying to use `torch.compile(model)`, the terminal exploded with massive warning logs:

```text
OutOfResources: out of resource: shared memory, Required: 294912, Hardware limit: 166912.
Reducing block sizes or `num_stages` may help.
```

**The Math:** 166,912 bytes is exactly **163 KB**—the exact physical SRAM capacity per Streaming Multiprocessor (SM) on an NVIDIA A100/H100 GPU. The Triton compiler was trying to optimize matrix multiplications by loading hyper-aggressive tile blocks (e.g., `BLOCK_M=64, BLOCK_N=128, BLOCK_K=128, num_stages=4`).

*   $((64 \times 128) + (128 \times 128)) \times 4\text{ bytes (float32)} = 96\text{ KB}$ per tile.
*   Pipelining with $4 \text{ stages}$ requested 3 buffering tiles concurrently: $96\text{ KB} \times 3 = \mathbf{288\text{ KB}}$.
*   **The Resolution:** This warning can be safely ignored or muted! PyTorch's autotuner automatically discards the configurations exceeding the 163 KB physical ceiling, finds a valid layout (e.g., `triton_mm_524` taking just `0.0123 ms`), and caches the baked kernels to `~/.cache/torch/inductor` for future runs.

---

## Step 3: Eliminating CPU-GPU Synchronization Traps

Even after the compiler stabilized, the second epoch was still taking 25+ minutes. The culprit was a highly inefficient tracking loop inside our epoch executor:

```python
# THE PERFORMANCE KILLER
for idx, databatch in enumerate(train_loader):
    ...
    loss.backward()
    optimizer.step()
    train_loss += loss.item() # <--- Graph Break & Sync Point!
    for comp_name, comp_value in zip(lcomps_names, lcomps):
        lcomps_train[comp_name].append(comp_value.item()) # <--- Hidden Sync Cascade!
```

### Why this kills speed:

Calling `.item()` or appending to native Python lists inside the batch loop forces a **Graph Break**. The CPU freezes and waits for the GPU to completely flush its pipeline just to copy a single float back to Python memory. Across 1,000 batches, this causes 4,000+ full hardware stalls.

### The Refactored Solution:

Pre-allocate tracking tensors directly on the GPU, keep them detached from the computational graph, and only move them to the CPU **once per epoch**.

```python
# HIGH PERFORMANCE LOOP
train_loss_log = torch.zeros(num_train_batches, device=DEVICE)

for idx, databatch in enumerate(train_loader):
    if idx >= num_train_batches: break
    x, target, ... = databatch
    x = x.to(DEVICE, non_blocking=True)
    target = target.to(DEVICE, non_blocking=True)
    
    optimizer.zero_grad()
    x_recon, zvars = model(x)
    loss = lossfunction(target, x_recon)
    loss.backward()
    optimizer.step()

    # Asynchronous GPU-to-GPU copy (No .item() stalls!)
    train_loss_log[idx] = loss.detach() 

# Move to CPU in one single block transfer after the loop finishes
rloss_train = train_loss_log.cpu().tolist()
```

---

## Step 4: Shattering the HDF5 Global Process Lock
When ramping up `num_workers > 0` to parallelize data ingestion, PyTorch threw a catastrophic dataloader failure:

```text
RuntimeError: _share_filename_: only available on CPU
TypeError: h5py objects cannot be pickled
```

This uncovered a compounding architectural flaw:

1.  Tensors were being instantiated on the GPU device (`.to(DEVICE)`) directly inside the `Dataset` items. Worker processes cannot serialize or pass GPU-resident memory objects back to the main process via standard pickling.
2.  The standard C-library behind `h5py` is **not thread-safe** and enforces an internal global lock. Opening the file handle once in `__init__` forced all data workers to queue up sequentially through a single CPU core, completely stalling the data pipeline.

### The Architecture Overhaul: "Open, Measure, Close"

We restructured the custom dataset to remain strictly on the CPU, pre-measure file parameters, and force worker processes to open their own isolated, high-speed file connections on-demand.

```python
class WorkerSafeWaveformDataset(torch.utils.data.Dataset):
    def __init__(self, hdf_fname):
        self.hdf_fname = hdf_fname
        
        # Open temporarily to get total samples, then immediately close
        with h5py.File(self.hdf_fname, 'r') as f:
            self.length = len(f.keys()) 
            
        self.data_file = None # Leave handle empty for safe pickling!

    def __len__(self):
        return self.length

    def read_data_from_hdf(self, idx):
        # Every worker opens its own isolated descriptor on first access
        if self.data_file is None:
            self.data_file = h5py.File(self.hdf_fname, 'r')
            
        data = self.data_file[f'sample{idx}']
        
        # Explicitly enforce CPU instantiation to bypass global device defaults
        input_data = torch.tensor(data['input'][:], device='cpu')
        target_data = torch.tensor(data['target'][:], device='cpu')
        
        return input_data, target_data
```

---

## Step 5: Saturation via Batch Size Expansion

With the parallel data-loading framework finally fixed, we increased the `DataLoader` configuration to **`num_workers=8`** and increased the batch size to **`128`**. 

This did two massive things simultaneously:
1.  **Saturated the Compute Cores:** Expanding the batch size gave the GPU enough raw matrix mathematics to stay fully occupied, maximizing streaming multiprocessor utilization.
2.  **Slashed Iteration Overhead:** It drastically minimized the frequency of Python-to-C++ loop boundary transitions per epoch.

---

## Step 6: Scaling Batch Sizes & Choosing the Right Scheduler

With the I/O pipeline cleared of bottlenecks, we can aggressively scale our execution parameters on the data center hardware (NVIDIA A100-80GB) while keeping training mathematically stable.

### 1. The Large Batch Size Transition (128 vs. 1024)

Moving from a batch size of 128 to **1024** is highly recommended **strictly on the cluster's A100s**. The massive memory architecture of an 80GB VRAM card thrives on wider matrices, allowing the Tensor Cores to reach peak mathematical throughput. However, keep the batch size at 128 for local development to avoid Out-Of-Memory (OOM) errors on local Unified Memory.

**The Linear Scaling Rule:** When you scale up your batch size by 8× (128 → 1024), the model updates its weights 8× less frequently per epoch. To compensate for this fewer number of steps, you **must scale up your base learning rate** (typically by 2× to 4× your small-batch baseline) to maintain gradient descent momentum.

### 2. The Verdict: Adaptive vs. Blind Scheduling

When managing complex gravitational-wave parameter estimation and VAE likelihood surfaces, **`ReduceLROnPlateau` is vastly superior** to a rigid `StepLR`.

```python
# CHOOSE THIS: Adaptive Monitoring
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
    optimizer, 
    mode='min', 
    factor=0.2,       # A 5x drop keeps optimization paths smoother than a harsh 10x cut
    patience=4,       # Expanded from 2 to 4 to tolerate natural large-batch fluctuations
    threshold=1e-4
)

# AVOID THIS: Blind Decays
# scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.1)
```

### Why `ReduceLROnPlateau` Wins for Scientific Models:

* **Context Awareness:** `StepLR` drops your learning rate on a fixed mathematical clock (e.g., exactly at Epoch 3), completely blind to whether your loss is still plummeting or has barely begun to warm up. 
* **Convergence Protection:** `ReduceLROnPlateau` acts as a dynamic supervisor. It waits until validation loss actively hits a plateau, respects your `patience` buffer, and only compresses the learning rate when the model genuinely stops making architectural progress.

### Implementing the Step Execution
Because `ReduceLROnPlateau` tracks performance metrics rather than epoch counts, its `.step()` call requires the current validation loss passed to it immediately following the evaluation phase:

```python
# Execution pattern at the very end of your validation loop
val_loss_avg = val_loss_log.mean().item()

# Update the scheduler with the latest metric
scheduler.step(val_loss_avg)

# Log the learning rate shift for tracking
current_lr = optimizer.param_groups[0]['lr']
logger.info(f"Epoch {epoch} finished. Current Learning Rate: {current_lr}")
```

---

## Final Performance Comparison

| Metric / Stage | Original Baseline | The Optimized Pipeline |
| :--- | :--- | :--- |
| **Data Ingestion** | Single-threaded Locked HDF5 | 8 Parallel Workers (No Lock) |
| **GPU/MPS Utilization** | Starved (~10-20% bursts) | Fully Saturated (Continuous) |
| **Graph Stalls** | 4,000+ `.item()` breaks / epoch | 0 Graph Breaks |
| **Total Epoch Duration** | **35 Minutes** | **3 Minutes** 🎉 |

By keeping data loading isolated on the CPU, removing file access concurrency constraints, keeping tracking arrays natively on the GPU device, and scaling up the batch size to fully utilize the processing cores, the pipeline is now completely optimized. The code can now seamlessly scale up to 100+ epochs on cluster allocations in a fraction of the time!

---

### Extra: Evading the "Monster Node" Core-Clamp in `tmux`

On dense high-performance computing (HPC) nodes boasting massive core topologies (e.g., Dual-Socket 256-thread systems), certain linear algebra backends (like Intel MKL or OpenBLAS) execute aggressive initialization routines that clamp the execution environment's thread-affinity down to a single core, tricking PyTorch's `DataLoader` into believing the host is single-threaded. Compounding this, running within a `tmux` workspace often isolates or discards shell-level initialization variables. To bypass this thread containment silently, variables must be bound at the **absolute entry point** of the Python runtime before any third-party framework loads:

```python
import os
# Force sub-libraries to yield thread management back to the OS
os.environ["KMP_AFFINITY"] = "disabled"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"

# Safe to proceed with high-performance framework initialization
import torch
import numpy as np
```
