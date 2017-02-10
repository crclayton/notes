import numpy 
from math import factorial

p = 0.10
N = 50000

vals = [(1,2), (2,1), (5,7), (7,5)]

def main():
    for i, j in vals:        
        n = i+j-1 
        x = i 
        print(1-sum([ choose(n, x)*(p**x)*(1-p)**(n-x) for i in range(x) ])  )

    b()
    c()    

def b():
    for i, j in vals:

        left_true = 0
        right_true = 0
        for x in range(N):
            trials = numpy.random.binomial(1, p, 500)

            if T(trials, j) > S(trials, i): 
                left_true += 1

            if numpy.random.binomial(i+j-1, p) >= i:
                right_true += 1
        
        print(tex(i, j, left_true/N, right_true/N, percent_difference(left_true/N, right_true/N)))

def c():
    failure_counts = []
    for i in range(N):
        trials = numpy.random.binomial(1, p, 500)
        successes = 0 
        failures = 0
        for result in trials:
            if result == 1:
                successes += 1
            else:
                failures += 1
            
            # not sure if this would actually make a difference
            if successes >= 20:
                failure_counts.append(failures)
                break 
    
    mu = numpy.mean(failure_counts)
    sigma = numpy.std(failure_counts)

    print(mu, sigma) 

# find the position of the list at which 
# there's the ith success (nonzero value)
def S(binary_list, i):
    successes = 0
    for position in range(len(binary_list)):
        if binary_list[position] == 1: 
            successes += 1
        if successes == i: 
            return position + 1
    raise Exception("Not correct position, list not long enough") 

# find the position of the list at which 
# there's the jth failure (zero value)
def T(binary_list, j):
    failures = 0
    for position in range(len(binary_list)):
        if binary_list[position] == 0: 
            failures += 1
        if failures == j: 
            return position + 1
    raise Exception("Not correct position, list not long enough") 

def percent_difference(a, b):
    try:
       return 100*abs(a - b)/a
    except ZeroDivisionError:
        return 0

def choose(n, r):
    if n < r : return 0
    return factorial(n) // factorial(r) // factorial(n-r)

# print out to allow easy copy and paste into LaTeX table
def tex(*args, dec=7):
    formatting = "%." + str(dec) + "f"
    l = [formatting % i for i in args]
    s = "\t&\t".join(l) + "\t\\\\"
    s = s.replace("." + "0" * dec ,"")
    return s

if __name__ == "__main__":
    main()


#OUTPUT
r"""
0.82
0.98
0.9877237129
0.9998484409
1	&	2	&	0.1896600	&	0.1884200	&	0.6538015	\\
2	&	1	&	0.0097800	&	0.0094200	&	3.6809816	\\
5	&	7	&	0.0028800	&	0.0025800	&	10.4166667	\\
7	&	5	&	0.0000600	&	0.0000200	&	66.6666667	\\
180.14172 42.0913140142
"""