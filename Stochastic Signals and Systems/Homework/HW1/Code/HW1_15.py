from random import randint
from math import factorial 

# return a random 0 or 1 
# pinball makes a choice to go left, 0 or right, 1
def choice():
    return randint(0,1)

# return a sequence of random choices of a given number
def sequence(n):
    return [choice() for i in range(n)]

# return the number of 1s in a sequence
# which is the position of the ball 
def position(arr):
    return arr.count(1)

# run N simulations to determine the 
# frequencies at which the ball is 
# positioned in each of a given number of slots
def frequencies(cells):
    counter = [0]*cells

    for i in range(N):
        pos = position(sequence(cells - 1))
        counter[pos] += 1

    return counter 


N = 1000


# print the results of the simulated and theoretical 
# position frequencies and their percent difference 
# for cells 0-4
real = [0.0625, 0.25, 0.375, 0.25, 0.0625]
for i, c in enumerate(frequencies(4)):
    print(i, "\t", c/N, "\t", real[i],  "\t", 100*abs(real[i]-c/N)/real[i])


# print the results of the simulated and theorital
# position frequencies and their percent difference
# for cells 0-100
p = 0.5
n = 100
for k, c in enumerate(frequencies(n)):
    theoretical = factorial(100)/(factorial(100-k)*factorial(k)) * (0.5**100)
    print(k, "\t", c/N, "\t", theoretical, "\t", round(100*abs(theoretical-c/N)/theoretical,6))

# OUTPUT
r"""
Running C:\Users\Charles Clayton\OneDrive\Documents\School\4th Year\ELEC 321 - Stochastic Signals and Systems\Homework\Homework1\Homework1\Homework1\main.py
0 	 0.112 	 0.0625 	 79.2
1 	 0.378 	 0.25 	 51.2
2 	 0.385 	 0.375 	 2.666666666666669
3 	 0.125 	 0.25 	 50.0
0 	 0.0 	 7.888609052210118e-31 	 100.0
1 	 0.0 	 7.888609052210118e-29 	 100.0
2 	 0.0 	 3.9048614808440084e-27 	 100.0
3 	 0.0 	 1.275588083742376e-25 	 100.0
4 	 0.0 	 3.093301103075262e-24 	 100.0
5 	 0.0 	 5.939138117904503e-23 	 100.0
6 	 0.0 	 9.403635353348797e-22 	 100.0
7 	 0.0 	 1.2627738903068384e-20 	 100.0
8 	 0.0 	 1.4679746474816996e-19 	 100.0
9 	 0.0 	 1.5005963063146263e-18 	 100.0
10 	 0.0 	 1.3655426387463099e-17 	 100.0
11 	 0.0 	 1.1172621589742536e-16 	 100.0
12 	 0.0 	 8.286361012392381e-16 	 100.0
13 	 0.0 	 5.609228993004073e-15 	 100.0
14 	 0.0 	 3.4857351599382454e-14 	 100.0
15 	 0.0 	 1.998488158364594e-13 	 100.0
16 	 0.0 	 1.0616968341311906e-12 	 100.0
17 	 0.0 	 5.246031415707059e-12 	 100.0
18 	 0.0 	 2.4190033750204773e-11 	 100.0
19 	 0.0 	 1.0439909302719954e-10 	 100.0
20 	 0.0 	 4.2281632676015815e-10 	 100.0
21 	 0.0 	 1.6107288638482216e-09 	 100.0
22 	 0.0 	 5.78398092018225e-09 	 100.0
23 	 0.0 	 1.9615239642357197e-08 	 100.0
24 	 0.0 	 6.2932227185896e-08 	 100.0
25 	 0.0 	 1.9131397064512386e-07 	 100.0
26 	 0.0 	 5.518672230147804e-07 	 100.0
27 	 0.0 	 1.5125249815960647e-06 	 100.0
28 	 0.0 	 3.9433687020183116e-06 	 100.0
29 	 0.0 	 9.790432639493739e-06 	 100.0
30 	 0.0 	 2.3170690580135184e-05 	 100.0
31 	 0.0 	 5.232091421320847e-05 	 100.0
32 	 0.0 	 0.00011281697127223077 	 100.0
33 	 0.001 	 0.00023247133474277857 	 330.160562
34 	 0.0 	 0.00045810527728724014 	 100.0
35 	 0.0 	 0.0008638556657416528 	 100.0
36 	 0.003 	 0.0015597393964779842 	 92.339823
37 	 0.002 	 0.0026979276047186754 	 25.869026
38 	 0.005 	 0.00447287997624412 	 11.784801
39 	 0.009 	 0.00711073226992655 	 26.569243
40 	 0.011 	 0.010843866711637987 	 1.43983
41 	 0.02 	 0.015869073236543397 	 26.031304
42 	 0.019 	 0.022292269546572867 	 14.76866
43 	 0.026 	 0.030068642644214563 	 13.531182
44 	 0.043 	 0.03895255978909614 	 10.390691
45 	 0.061 	 0.048474296626430755 	 25.839887
46 	 0.061 	 0.05795839814029764 	 5.247905
47 	 0.08 	 0.06659049999098027 	 20.137257
48 	 0.086 	 0.07352701040670738 	 16.96382
49 	 0.083 	 0.07802866410507722 	 6.371166
50 	 0.073 	 0.07958923738717877 	 8.279056
51 	 0.064 	 0.07802866410507722 	 17.97886
52 	 0.069 	 0.07352701040670738 	 6.156935
53 	 0.069 	 0.06659049999098027 	 3.618384
54 	 0.055 	 0.05795839814029764 	 5.104348
55 	 0.04 	 0.048474296626430755 	 17.482041
56 	 0.04 	 0.03895255978909614 	 2.689015
57 	 0.024 	 0.030068642644214563 	 20.182629
58 	 0.017 	 0.022292269546572867 	 23.74038
59 	 0.014 	 0.015869073236543397 	 11.778087
60 	 0.007 	 0.010843866711637987 	 35.447381
61 	 0.005 	 0.00711073226992655 	 29.683754
62 	 0.007 	 0.00447287997624412 	 56.498722
63 	 0.001 	 0.0026979276047186754 	 62.934513
64 	 0.003 	 0.0015597393964779842 	 92.339823
65 	 0.0 	 0.0008638556657416528 	 100.0
66 	 0.002 	 0.00045810527728724014 	 336.580869
67 	 0.0 	 0.00023247133474277857 	 100.0
68 	 0.0 	 0.00011281697127223077 	 100.0
69 	 0.0 	 5.232091421320847e-05 	 100.0
70 	 0.0 	 2.3170690580135184e-05 	 100.0
71 	 0.0 	 9.790432639493739e-06 	 100.0
72 	 0.0 	 3.9433687020183116e-06 	 100.0
73 	 0.0 	 1.5125249815960647e-06 	 100.0
74 	 0.0 	 5.518672230147804e-07 	 100.0
75 	 0.0 	 1.9131397064512386e-07 	 100.0
76 	 0.0 	 6.2932227185896e-08 	 100.0
77 	 0.0 	 1.9615239642357197e-08 	 100.0
78 	 0.0 	 5.78398092018225e-09 	 100.0
79 	 0.0 	 1.6107288638482216e-09 	 100.0
80 	 0.0 	 4.2281632676015815e-10 	 100.0
81 	 0.0 	 1.0439909302719954e-10 	 100.0
82 	 0.0 	 2.4190033750204773e-11 	 100.0
83 	 0.0 	 5.246031415707059e-12 	 100.0
84 	 0.0 	 1.0616968341311906e-12 	 100.0
85 	 0.0 	 1.998488158364594e-13 	 100.0
86 	 0.0 	 3.4857351599382454e-14 	 100.0
87 	 0.0 	 5.609228993004073e-15 	 100.0
88 	 0.0 	 8.286361012392381e-16 	 100.0
89 	 0.0 	 1.1172621589742536e-16 	 100.0
90 	 0.0 	 1.3655426387463099e-17 	 100.0
91 	 0.0 	 1.5005963063146263e-18 	 100.0
92 	 0.0 	 1.4679746474816996e-19 	 100.0
93 	 0.0 	 1.2627738903068384e-20 	 100.0
94 	 0.0 	 9.403635353348797e-22 	 100.0
95 	 0.0 	 5.939138117904503e-23 	 100.0
96 	 0.0 	 3.093301103075262e-24 	 100.0
97 	 0.0 	 1.275588083742376e-25 	 100.0
98 	 0.0 	 3.9048614808440084e-27 	 100.0
99 	 0.0 	 7.888609052210118e-29 	 100.0
"""