---
permalink: /
title: "Research"
math: true
hideAuthor: true
ShowWordCount: false
ShowToc: true
ShowReadingTime: false
hideTags: true
redirect_from: 
  - /research/
---

My PhD research focuses on gravitational-wave astrophysics, specifically modelling theoretical approximations for gravitational waveforms. Over the past few years, I have broadly worked on computational astrophysics and data analysis. Below is a brief description and summary of my research interests. Some projects have their own pages.

---

## Gravitational Waves Astrophysics

### Generating gravitational waveform approximations using machine learning models



- I build fast *surrogate* or data-driven waveform models for compact binaries, with the current aim of accurately approximating effective one-body waveforms, which would be later expanded into other waveforms approximations and binary systems.
- Architectures explored include convolutional networks on time–frequency representations and lightweight auto-encoder models for rapid evaluation.
- Targets: high overlap (low mismatch) with reference waveforms, large parameter-space coverage (incl. eccentricity and spin), and orders-of-magnitude better speed.
- Intended use cases: speeding up parameter estimation, tests of gravity with novel waveforms, data analysis from 3G gravitational wave detectors.

### Detections of gravitational waves from compact object mergers

- I developed deep-learning pipelines for detection/classification of compact binary coalescences and related sources.
- Training strategy comparisons (curriculum learning, transfer learning) to improve sensitivity and robustness to glitches.

---

## Stellar and Solar Physics

### Stellar magnetic cycles and variability

- Studied the **Waldmeier effect** (anti-correlation of rise time with cycle amplitude) in stellar activity cycles, extending solar-cycle variability studies to other stars.
- Methods included cycle identification, smoothing and function fits to probe long-term amplitude variations and correlations between stellar properties.
- Results aid in constraining solar dynamo model behaviors from the point of view of other Sun-like stars.

### Super-resolving the solar magnetograms

- Worked on super-resolution and denoising of solar magnetograms using convolutional models.
- Goals: recover small-scale magnetic structures from older low-resolution magnetograms by super-resolving the the low-resolution images.

---

## Other Interests

### AGNs and X-Ray Emissions

- Worked on developing pipeline for XMM-Newton EPIC instrument auto data reductions and inferences for a single query raw data to science products pathway.
- Analysed the ASASSN-14li data using the developed pipeline to check for a presence of X-Ray Corona formation in that system.


### Dark Matter Halos and the Uchuu simulation

- Brief stint on developing pipeline to calculate the halo occupancy number distribution in the Uchuu and Rockstar simulations.


### Internal structure of Neutron Stars

- Investigated tidal contributions to periastron precession in stellar-mass NS – BH binaries and found them *negligible* in the regimes considered, clarifying where strong-field GR effects dominate over tidal structure effects.

### Machine Learning

- Broad interest in physically-informed ML: data augmentation that respects symmetries, calibrated uncertainties, and attribution methods (e.g., Grad-CAM).
- Reproducible research and open-source: contributions within the scientific Python ecosystem (e.g., community tools for astronomy and relativity).
- Symbolic regression and machine learning physical symmetries from large-scale multimodal datasets.