# -*- coding: utf-8 -*-

from numpy import append, NINF, Inf

def trunc(dist, size=1, lower=NINF, upper=Inf):
    stringDist = dist[0:-1] + ', size=' + str(size) + ')'
    x = eval(stringDist)
    
    oob = (x < lower) | (x > upper) == False  #boolean array of out of bounds elements
    
    truncated = x[oob]  #in bounds elements
    
    while len(truncated) < size:
        y = eval(stringDist)
        oob = (y < lower) | (y > upper) == False
        
        newTruncated = y[oob]
        
        truncated = append(truncated, newTruncated)
    
    truncated = truncated[0:size]
        
    return truncated



