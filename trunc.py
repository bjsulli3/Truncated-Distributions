# -*- coding: utf-8 -*-

from numpy import append, NINF, Inf

def trunc(dist, size=1, lower=NINF, upper=Inf, ignore_warning=False):
    
    if lower > upper:
        raise ValueError('lower=' + str(lower) + ' must be less than upper=' +str(upper))
    
    stringDist = dist[0:-1] + ', size=' + str(size) + ')'
    x = eval(stringDist)
    
    oob = (x < lower) | (x > upper) == False  #boolean array of out of bounds elements
    
    truncated = x[oob]  #in bounds elements
    
    i=0
    while len(truncated) < size:
        y = eval(stringDist)
        oob = (y < lower) | (y > upper) == False
        
        newTruncated = y[oob]
        
        truncated = append(truncated, newTruncated)
        
        i += 1

        if i == 10000 and ignore_warning == False:
            raise RuntimeError('ensure shape and bound parameters are reasonable')
            
    truncated = truncated[0:size]
        
    return truncated

trunc('scipy.stats.uniform.rvs(loc=10, scale=10)', lower=23, upper=22, size=1000)

scipy.stats.uniform.rvs(loc=10, scale=10)
