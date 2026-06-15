---
author: "Suyog Garg"
title: "All about running jobs on Condor"
date: "2026-06-15"
tags:
    - condor
    - cluster
    - hpc
    - pe
---


**Disclaimer:** Based on Google Gemini-Pro prompts! 


# Demystifying HTCondor for Astrophysics: Scaling Parameter Estimation Without Losing Your Sanity

If you are a PhD student or researcher working in gravitational-wave astronomy, machine learning, or high-performance data analysis, you will eventually find yourself submitting jobs to a massive compute cluster like the LIGO Data Grid (LDG) or a local university cluster. At the heart of these environments sits **HTCondor**—a workload management system designed for High-Throughput Computing (HTC).

HTCondor is incredibly powerful; it can manage hundreds of thousands of concurrent tasks, running your parameter estimation campaigns (`bilby`, `dynesty`, `nessai`, `pocomc`) across thousands of CPU cores and GPUs seamlessly. 

However, HTCondor can also be deeply frustrating. One tiny trailing slash in a configuration path or a hidden file permission quirk can stall your entire campaign, putting dozens of your jobs into a dreaded `Held` state. 

This deep-dive guide covers how HTCondor operates under the hood, how to design efficient submit files, and the key pitfalls to avoid when running resource-intensive Python pipelines.

---

## 1. How HTCondor Works: The Architecture

To troubleshoot HTCondor effectively, you need to understand that your jobs are managed by three distinct processes communicating across a network:

[ Submit Machine ] [ Central Manager ]            [ Execute Worker Node ]
+------------------+            +-------------------+          +-----------------------+|  

| condor\_schedd   | ---------> |   condor\_collector| -------->|     condor\_startd     |

| (Tracks your queue)           |  (Matchmaker/Pool)|          | (Launches the starter)|
+------------------+            +-------------------+          +-----------------------+


1. **The Schedd (`condor_schedd`):** Runs on the submit/login machine. It maintains your job queue, tracks resource requests, and waits for a matching compute slot.
2. **The Collector (`condor_collector`):** The cluster's matchmaker. It scans available resources reported by compute nodes and pairs them with jobs waiting in the `schedd`.
3. **The Startd (`condor_startd`):** Runs on every remote worker node. It manages the physical execution slots and spawns an internal process called the `starter` to physically execute your shell script.

---

## 2. Structural Blueprint of an Optimized Submit File

When building a production-ready `.sub` script, your goal is to make it as explicit and robust as possible. Below is a blueprint designed for machine learning inference and sampling jobs:

```condor
# ==============================================================================
# HTCondor Parameter Estimation Submission Template
# ==============================================================================

# Explicitly set the base directory to avoid relative path confusion
initialdir              = /home/username/phd-main/umami

# Executable configuration (The shell wrapper that sets up Python)
executable              = $(initialdir)/condor-run-inference.sh
arguments               = ml2ml-paper-1 $(Process) pocomc ml2ml 1024 0.2 4 1

# Output File Routing (Crucial for streaming logs)
output                  = logs/inference_$(Cluster)_$(Process).out
error                   = logs/inference_$(Cluster)_$(Process).err
log                     = logs/inference_$(Cluster).log

# Environment & File Transfer Strategies
universe                = vanilla
getenv                  = True
should_transfer_files   = YES
when_to_transfer_output = ON_EXIT

# Fine-Tuned Resource Requests (Avoid over-requesting!)
request_cpus            = 8
request_memory          = 8GB
request_disk            = 2GB

# Safety Node Filters
requirements            = (Machine =!= "node2299.cluster.ldas.cit")

# Queue the jobs (e.g., runs the arguments macro 100 times from 0 to 99)
queue 100
```

---

## 3. High-Utility Pitfalls & Diagnostic Manual

When running parameter estimation loops paired with PyTorch or intensive samplers, watch out for these four common failure scenarios:

### Pitfall 1: The Network File System (NFS) Sync Lag
* **The Symptom:** Your jobs fail instantly on random worker nodes with `No such file or directory (errno 2)` targeting your `.out` or `.err` path, even though the directory exists on your login machine.
* **The Cause:** Compute clusters use a distributed Network File System (NFS). When you create a new directory (like `logs/`) on the login machine, it takes a few moments to sync out to the worker nodes. If a node picks up your job before its NFS cache refreshes, it crashes because it cannot open the output text stream.
* **The Solution:** Avoid absolute network home paths for streaming outputs, or utilize the `should_transfer_files` syntax. By declaring your outputs relative to the temporary workspace:
  ```condor
  output = inference_$(Cluster)_$(Process).out
  ```
  HTCondor will stream the logs to the worker node's physical local drive (`/var/lib/condor/execute/...`), completely bypassing network file system latency. The files are then safely packaged and transferred back to your home folder upon successful completion.

### Pitfall 2: Lost Executable Permissions (`errno 13: Permission Denied`)
* **The Symptom:** Your job enters the `Held` state immediately with `Failed to execute ... (errno=13: 'Permission denied')`.
* **The Cause:** If you edit your shell script (`.sh`) using an external IDE like VS Code or move files across directories, the file system can strip out the binary execution bit (`-rw-r----` instead of `-rwxr-xr-x`).
* **The Solution:** You must explicitly restore execution permissions in your terminal before running a submission:
  ```bash
  chmod +x /path/to/your/condor-run-inference.sh
  ```
  You can then wake up all held jobs in the queue using a target constraint flag:
  ```bash
  condor_release -constraint 'JobStatus == 5 && HoldReasonCode == 6'
  ```

### Pitfall 3: The "Pickle Tax" vs. PyTorch Thread Conflicts
* **The Symptom:** You add `npool=8` to your python script thinking it will make your sampler 8x faster, but the code actually runs significantly *slower* or hangs entirely.
* **The Cause:** Python multiprocessing requires data to be serialized ("pickled") and sent over operating system pipes. For very fast machine learning likelihood functions, this communication overhead wastes valuable CPU cycles. Even worse, if your PyTorch model tries to spawn internal multi-threading loops inside an already multi-processed worker pool, the CPU cores will thrash against each other.
* **The Solution:** Drop multiprocessing workers (`npool=1`) and exploit internal tensor parallelism instead. Send your parameters to your model as a single large batch matrix and instruct PyTorch to multi-thread the calculation directly across the cores at a native C++ level. At the top of your execution script, configure the environment variables properly:
  ```python
  import os
  import torch
  os.environ["OMP_NUM_THREADS"] = "8"
  os.environ["MKL_NUM_THREADS"] = "8"
  torch.set_num_threads(8)
  ```

### Pitfall 4: Bad Resource Request Ratios (The Queue Trap)
* **The Symptom:** Your jobs are stuck in the `Idle` state for hours, or they get evicted during intensive sampling phases.
* **The Cause:** Over-requesting resources (like asking for 24 GB of RAM when your model only touches 4.9 GB) forces the matchmaker to look for massive, rare slots, keeping you stuck in the queue. Conversely, under-requesting causes the cluster to kill your process the moment your neural network runs a training pass or a dense gradient evaluation that spikes over the limit.
* **The Solution:** Inspect a successfully completed log file to check the real resource tracking stats:
  ```text
  Partitionable Resources :    Usage  Request Allocated
     Memory (MB)          :     4909    24576     24576
  ```
  Identify the exact peak `Usage`, add a safe 30% margin, and match your request to the natural hardware layout of the cluster nodes (typically 2 GB of RAM per CPU core) to ensure rapid scheduling.

---

## 4. Essential HTCondor Cheat Sheet

| Command | Action |
| :--- | :--- |
| `condor_q` | View your active running queue. |
| `condor_q -hold` | Display the exact reason why a job is stuck or held. |
| `condor_q -better-analyze <JobID>` | Detailed diagnostic breakdown of why a job won't match to a node. |
| `condor_history -limit 10 -af ClusterId MemoryUsage DiskUsage_RAW` | Review resource metrics for your last 10 completed runs. |
| `condor_qedit -constraint 'JobStatus==5' Output '"/fixed/path.out"'` | Mass-edit parameters for held jobs directly in the active queue. |
| `condor_rm -all` | Instantly kill all of your active and idle jobs. |

By mastering file routing, keeping your resource requests aligned with actual usage metrics, and leveraging native PyTorch threading over messy Python multiprocessing pools, you can run large-scale inference and sampling jobs reliably without dealing with constant node evictions. 

### 5. Deep-Dive: PyTorch Threading vs. Multiprocessing (And Why It Dictates Your Speed)

When building an ML-accelerated parameter estimation pipeline, deciding *how* to distribute your workload across your `request_cpus = 8` allocation will make or break your throughput. Misconfiguring this setting is the single most common reason cluster jobs run up to 10x slower than local benchmark runs.

To understand why, we have to look at how data flows under the hood in both paradigms.

#### Architectural Breakdown

[ STRATEGY A: Python Multiprocessing (npool=8) ]Main Process (Tracks Swarm)|-- (Pickle Data) --> Worker 1 (Copy of Model in RAM) --> Eval 1|-- (Pickle Data) --> Worker 2 (Copy of Model in RAM) --> Eval 2|-- (Pickle Data) --> Worker 3 (Copy of Model in RAM) --> Eval 3* Deep Bottleneck: Constant serialization/deserialization over OS pipes.* Massive RAM Waste: 8 workers * 500MB Model = 4GB redundant RAM footprint.[ STRATEGY B: Vectorized PyTorch Threading (npool=1 + torch.set_num_threads(8)) ]Main Process (Sends 1 Single Matrix Tensor of ALL particles)|vPyTorch C++ Backend Engine (MKL / OpenMP / ATen)|-- Core 1 Matrix Math Sub-Task \|-- Core 2 Matrix Math Sub-Task  |-- Zero Copying!|-- Core 3 Matrix Math Sub-Task  |-- Shares same physical memory pointers.|-- Core 4 Matrix Math Sub-Task /   -- Bypasses Python GIL completely.


#### The "Pickle Tax" and Core Contention

If you choose **Strategy A** (`npool=8`) with a non-vectorized sampler, you isolate each CPU core into its own independent operating system process. Because Python processes cannot share memory addresses natively:

1. The main sampler process must **serialize (pickle)** a parameter dictionary.
2. It pushes that raw byte stream through an OS pipe to Worker Core 3.
3. Worker Core 3 **unpickles** the data, passes it into its own independent copy of the 500 MB PyTorch model, grabs the scalar output float, **re-pickles it**, and pipes it back.

If your neural network inference pass is highly optimized and takes only 2 milliseconds, but the operating system overhead to package, pipe, and unpackage the data takes 5 milliseconds, **your CPUs spend more time talking than doing math.**

Even worse, if you leave PyTorch's default behavior untouched, *each* of those 8 workers will try to spawn internal C++ threads to use the remaining cores. Suddenly, 64 virtual threads are aggressively fighting for 8 physical CPU slots (**Core Oversubscription**), causing the operating system scheduler to choke and grinding your execution throughput down to a halt.

#### The Vectorized Solution

**Strategy B** completely eliminates this translation layer. By setting `vectorized=True` (in `pocomc`) and pairing it with a single worker pool (`npool=1`), you change the data flow entirely:

1. The sampler takes the entire pool of parameters and packages them into a single continuous 2D matrix structure.
2. It sends that **one single memory pointer** down to your PyTorch model.
3. PyTorch completely releases the Python Global Interpreter Lock (GIL) and drops into its low-level, compiled C++ backend (`Aten`/`MKL`/`OpenMP`).
4. The backend automatically carves up that huge matrix into parallel mathematical sub-tasks and drops them cleanly onto your 8 CPU threads.

Because all 8 threads read and write to the exact same physical memory block simultaneously, the data overhead drops to zero. Your throughput scales linearly with your core count, turning long, agonizing parameter estimation runs into highly efficient operations that finish in minutes.

Happy sampling!
