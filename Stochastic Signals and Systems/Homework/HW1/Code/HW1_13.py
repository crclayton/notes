from random import randint, choice
import numpy 
from math import factorial

N = 10000

# function to return (n choose r)
def choose(n, r):
    if n < r : return 0
    return factorial(n) // factorial(r) // factorial(n-r)

# make a random selection from an array
def random_selection(array):
    return choice(array)

# for a given nunmber of selections
# take a random selection from the array
# and return the minmum
def smallest_selection(array, selections):
    sels = []
    for i in range(selections):
        sels.append(random_selection(array))
    return min(sels) 

# simulate (a) to check calculated mean/variance 
# matches a calculated version
def a():
    Ys = []
    for i in range(N):
        chips = list(range(1,100+1)) 
        Y = random_selection(chips)
        Ys.append(Y)

    print("A")
    print(numpy.mean(Ys), numpy.var(Ys))

 
# simulate (b) to check calculated mean/variance
# matches a simulated  version
n = 100000

def f(a):
    return choose(100-a,5)/choose(100,5)

def b():
    chips = range(1,100+1)

    b = 0
    bns = []

    mu_s = 0
    var_s = 0

    mu_c = 0
    var_c = 0


    for x in range(1,100+1):

        # run n simulations taking smallest selection 
        # and seeing the proportion that it matches 
        # the given number x
        for i in range(n):
            s = smallest_selection(chips, 5)
            if s == x: 
                b += 1

        bns.append(1-b/n)

        # increament simulated mean and distribution 
        mu_s += 1-b/n        
        var_s += (1-b/n)* ((1-95/6))**2 # this equation doesn't seem to be right

        # increment theortical mean and distribution
        mu_c += f(x)
        var_c += f(x) * ((x-95/6))**2 # this equation doesn't seem to be right

    print("B")

    # theoritical mean and distrubition using pmf and cdf
    print(mu_c, var_c)

    # manually calculeted mean and distribution of simulation
    print(mu_s, var_s)

    # mean and distribution of simulation using numpy library 
    print(numpy.mean(bns), numpy.var(bns))

a()
b()

# OUTPUT
r"""
Running C:\Users\Charles Clayton\OneDrive\Documents\School\4th Year\ELEC 321 - Stochastic Signals and Systems\Homework\Homework1\Homework1\Homework1\main.py
A
50.409 826.435319
B
15.833333333333341 2332.0866402116403
16.425070000000023 3613.9716519444414
0.1642507 0.0594168596445
"""