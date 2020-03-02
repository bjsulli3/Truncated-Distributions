# -*- coding: utf-8 -*-

from numpy import random, append
from scipy import stats


def trunc(dist, size=1, lower=np.NINF, upper=np.Inf):
    stringDist = dist[0:-1] + ', size=' + str(size) + ')'
    x = eval(stringDist)
    
    oob = (x < lower) | (x > upper) == False  #boolean array of out of bounds elements
    
    truncated = x[oob]  #in bounds elements
    
    while len(truncated) < size:
        y = eval(stringDist)
        oob = (y < lower) | (y > upper) == False
        
        newTruncated = y[oob]
        
        truncated = append(truncated, newTruncated)
    
    truncated = truncated[0:size-1]
        
    return truncated

sample = trunc(size=10000, lower=15, upper=18, dist='stats.uniform.rvs(loc=10, scale=20)')


