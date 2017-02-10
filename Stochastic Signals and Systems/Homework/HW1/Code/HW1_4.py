
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
def consecutive_zeros(l):
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
        if(not consecutive_zeros(l)): nf += 1
    return nf

# list the number of bits 
# and the number that have consequtive zeros (two antennas down)
rows = 20
for n in range(0, rows):
    combinations = 2**n
    no_consequtives = number_with_consecutive_zeros(n)
    print(n, combinations, no_consequtives)

#OUTPUT
r"""
0 1 1 
1 2 2 
2 4 3 
3 8 5 
4 16 8
5 32 13 
6 64 21 
7 128 34 
8 256 55 
9 512 89 
10 1024 144 
11 2048 233 
12 4096 377 
13 8192 610 
14 16384 987 
15 32768 1597 
16 65536 2584 
17 131072 4181 
18 262144 6765 
19 524288 10946 
"""