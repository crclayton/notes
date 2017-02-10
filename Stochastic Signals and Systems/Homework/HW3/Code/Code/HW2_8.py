import numpy, scipy.stats, math 
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def pnorm(a):
    return scipy.stats.norm.cdf(a)

tolerance = 0.1
n = 1000000
"""
# determine the mean

for mean in numpy.arange(0.5102,0.512,0.00000001):
    std_dev = 0.1*mean
    

    dist = numpy.random.normal(loc=mean, scale=std_dev, size=n)

    too_sml = numpy.array(numpy.where(dist < mean-tolerance)).size
    too_big = numpy.array(numpy.where(dist > mean+tolerance)).size
    num_in_spec = (n - too_sml) - too_big

    simulated_percent = num_in_spec/n
    calculated_percent = 2*pnorm(tolerance/std_dev)-1

    print(mean, simulated_percent, calculated_percent) 

    if calculated_percent < 0.95: break
"""

def pnorm(a):
    return scipy.stats.norm.cdf(a)


flagged=False 
step = 0.0000001
tolerance = 0.000001

for mean in numpy.arange(101.5365, 105, step):
    for std_dev in numpy.arange(6.6042, 10, step):
        c1 = 1 - pnorm((105-mean)/std_dev)
        c2 = 1 - pnorm((110-mean)/std_dev)
        if 0.3-tolerance < c1 < 0.3+tolerance and 0.1-tolerance < c2 < 0.1+tolerance: 
            flagged = True
            print(mean, std_dev, c1, c2)
    
        if flagged: break 
    if flagged: break 

"""
# determine it again 

for mean in numpy.arange(90,110,0.1):
    for std_dev in numpy.arange(0,10,0.1):

        domain = numpy.arange(0, 200, 1)
        norm = scipy.stats.norm.pdf(domain, mean, std_dev)
        total = sum(norm)

        c1 = sum([norm[i] for i in range(len(domain)) if  domain[i] >= 105])
        c2 = sum([norm[i] for i in range(len(domain)) if  domain[i] >= 110])
        
        print(mean, std_dev, "30%:", c1/total, "10%:", c2/total)

        if 0.29 < c1/total < 0.31 and 0.09 < c2/total < 0.11: break

"""

"""
# confirm the mean
mean = 0.51021345
std_dev = 0.1*mean

domain = numpy.arange(0.3, 0.7, 0.00001)
norm   = scipy.stats.norm.pdf(domain, mean, std_dev)

total   = sum(norm)
in_spec = sum([norm[i] for i in range(len(domain)) if (mean-0.1) < domain[i] < (mean+0.1)])
print(in_spec/total)

plt.plot(domain, norm)
plt.show()
"""