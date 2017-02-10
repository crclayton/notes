
# return a list of 0s and 1s representing
# the binary of the given number
def binary_list(num, bits):
    u = format(num, "0" + str(bits) + "b")
    return [int(d) for d in u] 

# create a list of all combinations of 1s and 0s
# by counting in binary
def binary_list_sequence(bits):
    l = []
    for i in range(0, 2**(bits)):
        l.append(binary_list(i, bits))
    return l

# provided a list of 1s and 0s, detect 
# if the list contains consequtive zeros
def has_consecutive_zeros(l):
    for i in range(len(l) - 1):
        if(l[i] == 0 and l[i+1] == 0):
            return True
    return False

# given a number of bits, this will
# generate all the possible combinations
# of ones and zeros and determine the 
# number of which that have consequtive zeros
def number_with_consecutive_zeros(bits):
    nf = 0
    for l in binary_list_sequence(bits):
        if(not has_consecutive_zeros(l)): nf += 1
    return nf

# list the number of bits (heads/tails)
# and the number that have consequtive zeros
rows = 25
for n in range(rows+1):
    combinations = 2**n
    no_consequtives = number_with_consecutive_zeros(n)
    probability = no_consequtives/combinations    
    print(n, combinations, no_consequtives, probability)

#OUTPUT
r"""
Running C:\Users\Charles Clayton\OneDrive\Documents\School\4th Year\ELEC 321 - Stochastic Signals and Systems\Homework\Homework1\Homework1\Homework1\main.py
0 1 1 1.0
1 2 2 1.0
2 4 3 0.75
3 8 5 0.625
4 16 8 0.5
5 32 13 0.40625
6 64 21 0.328125
7 128 34 0.265625
8 256 55 0.21484375
9 512 89 0.173828125
10 1024 144 0.140625
11 2048 233 0.11376953125
12 4096 377 0.092041015625
13 8192 610 0.074462890625
14 16384 987 0.06024169921875
15 32768 1597 0.048736572265625
16 65536 2584 0.0394287109375
17 131072 4181 0.03189849853515625
18 262144 6765 0.025806427001953125
19 524288 10946 0.020877838134765625
20 1048576 17711 0.016890525817871094
21 2097152 28657 0.013664722442626953
22 4194304 46368 0.01105499267578125
23 8388608 75025 0.008943676948547363
24 16777216 121393 0.007235586643218994
25 33554432 196418 0.005853712558746338
"""
