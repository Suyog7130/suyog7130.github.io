---
title: 'How to install `gwpopulation` on MacOS'
date: 2025-03-11
place: Melbourne, Australia
tags:
  - software
  - research
---

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

- The error arises due to package dependency conflicts. See the references for further discussions.




References:

- https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
- https://github.com/bilby-dev/bilby/issues/917 

