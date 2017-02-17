import numpy, scipy.stats, math 
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def pnorm(a):
    return scipy.stats.norm.cdf(a)

tolerance = 0.1
n = 1000000

flagged=False 
step = 0.0000001
tolerance = 0.00001

for mean in numpy.arange(101.5365, 105, step):
    for std_dev in numpy.arange(6.6042, 10, step):
        c1 = 1 - pnorm((105-mean)/std_dev)
        c2 = 1 - pnorm((110-mean)/std_dev)
        if 0.3-tolerance < c1 < 0.3+tolerance and 0.1-tolerance < c2 < 0.1+tolerance: 
            flagged = True
            print(mean, std_dev, c1, c2)
    
        if flagged: break 
    if flagged: break 

#OUTPUT
r"""
101.5365 6.6043224 0.299990000065 0.100007433035
"""
