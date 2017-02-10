import numpy, scipy.stats, math 

mean = 1
std_dev = 0.1
n = 1000000

p = 0.77453754479968506
n_wafers = 200

between_counter = 0
for i in range(n): 
    norm = numpy.random.normal(loc=mean, scale=std_dev, size=n_wafers)
    n_good = sum(1 for i in range(n_wafers) if 0.85 < norm[i] < 1.1)

    if 140 < n_good < 160: 
        between_counter += 1
 
print(n_good, n_wafers, between_counter/n)

# OUTPUT
r"""
152 200 0.770507
"""