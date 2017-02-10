from random import randint 

def compute(S):
    n = 10              # n tests
    pi = [None]*(n+1)   # probability of event of interest, part is defective
    pi[0] = 0.15

    for k in range(1, n+1):
        # sequential Bayes' formula 
        if S[k-1] == 1: 
            a = p[k - 1 ]
            b = q[k - 1]
        else:
            a = 1 - p[k - 1]
            b = 1 - q[k - 1]

        pi[k] = a*pi[k-1] / ( a*pi[k-1] + b*(1-pi[k-1]) ) 

        print( round(pi[k], 4) , end="\t&\t")
  
    print(r"\\")

    return pi



# True indicates a positive test, False indicates a negative test
B1 = [True,  False, True,  False, True,  True,  True,  False, False, True ]
B2 = [True,  True,  True,  False, False, True,  False, False, False, False]
B3 = [False, False, False, True,  True,  False, True,  True,  True,  True ]
parts = [B1, B2, B3]

p = [0.80, 0.64, 0.86, 0.80, 0.74, 0.76, 0.77, 0.84, 0.85, 0.75]
q = [0.20, 0.16, 0.07, 0.09, 0.18, 0.13, 0.17, 0.14, 0.21, 0.08]

for B in parts:
    compute(B)    

# OUTPUT
r"""
Running C:\Users\Charles Clayton\OneDrive\Documents\School\4th Year\ELEC 321 - Stochastic Signals and Systems\Homework\Homework1\Homework1\Homework1\main.py
0.4138	&	0.2323	&	0.788	&	0.4496	&	0.7705	&	0.9515	&	0.9889	&	0.943	&	0.7585	&	0.9672	&	\\
0.4138	&	0.7385	&	0.972	&	0.884	&	0.7074	&	0.9339	&	0.7966	&	0.4215	&	0.1215	&	0.0362	&	\\
0.0423	&	0.0186	&	0.0028	&	0.0247	&	0.0942	&	0.0279	&	0.115	&	0.4381	&	0.7594	&	0.9673	&	\\
"""