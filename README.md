# Truncated-Distributions

This repository contains an easy to use function to sample from truncated distributions in Python. This functionality is well supported in the R and Julia ecosystems, but I have found the Python implementations lacking. This function supports the APIs found in numpy.random and scipy.stats.

The `trunc()` function takes four arguments:
  
  - `dist` / a string of a numpy.random or scipy.stats distribution reference, the size parameter should be excluded
  - `lower=np.NINF` / optional, the lower bound to sample within
  - `upper=np.Inf` / optional, the upper bound to sample within
  - `size=1` / optional, the number of samples to take
  
## Examples:

#### from scipy.stats.uniform

`trunc('scipy.stats.uniform.rvs(loc=10, scale=20)', lower=15, upper=18, size=1000)`

#### from numpy.random.lognormal

`trunc('numpy.random.lognormal(mean=0, sigma=1)', lower=0.5, upper=2, size=1000)`
