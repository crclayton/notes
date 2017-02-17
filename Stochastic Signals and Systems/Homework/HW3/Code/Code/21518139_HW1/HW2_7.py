import numpy, scipy.stats, math 


def pnorm(a):
    return scipy.stats.norm.cdf(a)

mean = 70
std_dev = 10

domain = numpy.arange(-200, 300, 0.0001)
norm = scipy.stats.norm.pdf(domain, mean, std_dev)
total = sum(norm)
in_spec = sum([norm[i] for i in range(len(domain)) if  domain[i] < 60])
print(total, in_spec, in_spec/total, pnorm((60-mean)/std_dev))


#OUTPUT
r"""
9999.99999966 1586.54044283 0.158654044289 0.158655253931
"""