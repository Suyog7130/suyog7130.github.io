---
title: 'How to install gwpopulation on MacOS'
date: 2025-03-11
place: Melbourne, Australia
tags:
  - software
  - research
---

### Basic `gwpopulation` installation

To install `gwpopulation` do:

- Create a new Conda environment :
`conda create --name monash`

- Activate the new environment :
`conda activate monash`

- Use `conda-forge` to install `gwpopulation` :
`conda install -c conda-forge gwpopulation`

- Check if import the installed package works or not :
`python3 -> import gwpopulation`

- Maybe there is a package dependency conflict and the import doesn't work ! Perhaps, it's the following error that pops up :

```python
❯ python3
Python 3.13.2 | packaged by conda-forge | (main, Feb 17 2025, 14:02:48) [Clang 18.1.8 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import gwpopulation
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    import gwpopulation
  File "/opt/homebrew/anaconda3/envs/monash/lib/python3.13/site-packages/gwpopulation/__init__.py", line 14, in <module>
    from . import conversions, hyperpe, models, utils, vt
  File "/opt/homebrew/anaconda3/envs/monash/lib/python3.13/site-packages/gwpopulation/hyperpe.py", line 48, in <module>
    from bilby.core.likelihood import Likelihood
  File "/opt/homebrew/anaconda3/envs/monash/lib/python3.13/site-packages/bilby/__init__.py", line 21, in <module>
    from . import core, gw, hyper
  File "/opt/homebrew/anaconda3/envs/monash/lib/python3.13/site-packages/bilby/core/__init__.py", line 1, in <module>
    from . import grid, likelihood, prior, result, sampler, series, utils, fisher
  File "/opt/homebrew/anaconda3/envs/monash/lib/python3.13/site-packages/bilby/core/grid.py", line 6, in <module>
    from .prior import Prior, PriorDict
  File "/opt/homebrew/anaconda3/envs/monash/lib/python3.13/site-packages/bilby/core/prior/__init__.py", line 1, in <module>
    from .analytical import *
  File "/opt/homebrew/anaconda3/envs/monash/lib/python3.13/site-packages/bilby/core/prior/analytical.py", line 3, in <module>
    from scipy.special._ufuncs import xlogy, erf, log1p, stdtrit, gammaln, stdtr, \
        btdtri, betaln, btdtr, gammaincinv, gammainc
ImportError: cannot import name 'btdtri' from 'scipy.special._ufuncs' (/opt/homebrew/anaconda3/envs/monash/lib/python3.13/site-packages/scipy/special/_ufuncs.cpython-313-darwin.so)
```

- Check if `bilby` can be imported :
`python3 -> import bilby`
Perhaps, it also has the same error.

- The error arises due to package dependency conflicts. See the references for further discussions. If a particular version or pre-release of `bilby` is required, you need to install it correctly.

### Installing `gwpopulation` from the Source

If the errors persist and you cannot find the possible culprits, then do a source install for `gwpopulation` by cloning the source repository, instead of the `pip` or `conda` install. This is helpful because maybe the latest version of the release already resolves the unknown error you get. Source installation can be done as:

```bash
   $ git clone git@github.com:ColmTalbot/gwpopulation.git
   $ cd gwpopulation/
   $ pip install -r requirements.txt
   $ pip install .
```


### Bilby "number of threads" Error

Due to setup of Bilby, the number of threads keywords has to be set manually, otherwise the following error pops up:

```bash
(monash) [suyog.garg@ldas-pcdev12 skewnorm_gw]$ python skewnorm.py config.ini
loading posteriors...
 43%|█████████████████████████████████▏                                           | 62/144 [00:00<00:00, 120.09it/s]excluding /home/rp.o4/catalogs/GWTC-4/FourthDraftRelease/5b450400_362/IGWN-GWTC4-5b450400_362-GW230518_125908-IllustrativeResult_PEDataRelease.hdf5
GW230518_125908 maximum mass_2_source < 3
excluding /home/rp.o4/catalogs/GWTC-4/FourthDraftRelease/5b450400_362/IGWN-GWTC4-5b450400_362-GW230529_181500-IMRPhenomXPHM_PEDataRelease.hdf5
GW230529_181500 maximum mass_2_source < 3
 81%|█████████████████████████████████████████████████████████████▊              | 117/144 [00:00<00:00, 164.37it/s]excluding /home/rp.o4/catalogs/GWTC-4/FourthDraftRelease/5b450400_362/IGWN-GWTC4-5b450400_362-GW231123_135430-NRSur7dq4_PEDataRelease.hdf5
GW231123_135430 in excldue
100%|████████████████████████████████████████████████████████████████████████████| 144/144 [00:00<00:00, 149.68it/s]
loading injections...
converting PE priors to chi_eff, chi_p ...
converting inj priors to chi_eff, chi_p ...
23:01 bilby INFO    : Running for label 'O4a', output will be saved to './skewnorm_dynesty_jax_o1o2o3o4_chieff_chip_offline_pe'
23:02 bilby INFO    : Analysis priors:
23:02 bilby INFO    : lamb=Uniform(minimum=-6, maximum=6, name='lamb', latex_label='$\\kappa_z$', unit=None, boundary=None)
23:02 bilby INFO    : alpha=Uniform(minimum=-4, maximum=12, name=None, latex_label='$\\alpha$', unit=None, boundary=None)
23:02 bilby INFO    : beta=Uniform(minimum=-4, maximum=12, name='beta', latex_label='$\\beta_{q}$', unit=None, boundary=None)
23:02 bilby INFO    : mmax=Uniform(minimum=30, maximum=100, name='mmax', latex_label='$m_{\\max}$', unit=None, boundary=None)
23:02 bilby INFO    : mmin=Uniform(minimum=2, maximum=10, name='mmin', latex_label='$m_{\\min}$', unit=None, boundary=None)
23:02 bilby INFO    : delta_m=Uniform(minimum=0.01, maximum=10, name='delta_m', latex_label='$\\delta_{m}$', unit=None, boundary=None)
23:02 bilby INFO    : lam=Uniform(minimum=0, maximum=1, name='lam', latex_label='$\\lambda_{peak}$', unit=None, boundary=None)
23:02 bilby INFO    : mpp=Uniform(minimum=20, maximum=50, name='mpp', latex_label='$\\mu_{peak}$', unit=None, boundary=None)
23:02 bilby INFO    : sigpp=Uniform(minimum=1, maximum=10, name='sigpp', latex_label='$\\sigma_{peak}$', unit=None, boundary=None)
23:02 bilby INFO    : mu_chi_eff=Uniform(minimum=-1, maximum=1, name='mu_chi_eff', latex_label='$\\mu_{eff}$', unit=None, boundary=None)
23:02 bilby INFO    : sigma_chi_eff=Uniform(minimum=0.01, maximum=4, name='sigma_chi_eff', latex_label='$\\sigma_{eff}$', unit=None, boundary=None)
23:02 bilby INFO    : eta_chi_eff=Uniform(minimum=-20, maximum=20, name='eta_chi_eff', latex_label='$\\eta_{eff}$', unit=None, boundary=None)
23:02 bilby INFO    : mu_chi_p=Uniform(minimum=0.01, maximum=1.0, name='mu_chi_p', latex_label='$\\mu_{p}$', unit=None, boundary=None)
23:02 bilby INFO    : sigma_chi_p=Uniform(minimum=0.01, maximum=1.0, name='sigma_chi_p', latex_label='$\\sigma_{p}$', unit=None, boundary=None)
23:02 bilby INFO    : Analysis likelihood class: <class 'gwpopulation.experimental.jax.JittedLikelihood'>
23:02 bilby INFO    : Analysis likelihood noise evidence: nan
2025-03-18 23:02:04.075362: F external/xla/xla/tsl/platform/default/env.cc:76] Check failed: ret == 0 (11 vs. 0)Thread tf_foreach creation via pthread_create() failed.
Aborted (core dumped)
```

This can be resolved by adding the following keywords to your `~/.bashrc` or `~/.zsh` profile or by setting them in the terminal:

```bash
# `bibly` keywords to limit number of threads
export OMP_NUM_THREADS=16
export OMP_PLACES="{0}:16"
export XLA_PYTHON_CLIENT_PREALLOCATE=false
```
After this, execute your python routines using `taskset -c 0-3 python <file-name>`



#### References:

- https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
- https://github.com/bilby-dev/bilby/issues/917 

