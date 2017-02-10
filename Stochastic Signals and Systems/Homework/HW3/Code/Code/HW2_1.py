import matplotlib.pyplot as plt
import numpy, random 

N_sims = 1000
n = 10000
T = 5
p = 0.0288
pool_sizes = [1000, 500, 200, 100, 50, 25, 20, 10, 8, 5]

def main():
    # calculate using probabilities
    for j, m in enumerate(pool_sizes):
        k = n/m 
    
        x1 = T
        p1 = (1.0-p)**m

        x2 = T*(m+1)
        p2 = 1-(1-p)**m

        ex = x1*p1 + x2*p2        

        ex2 = p1*(x1**2) + p2*(x2**2) 
        var = ex2 - ex**2 

        etk = k*ex 
        vartk = k*var 

        print(tex(j+1, k, m, ex, var, etk, vartk))

    tests = []

    # simulate 'n' tests with random sequences of approximately p 
    for m in pool_sizes:
        simulation_costs = []
        for i in range(N_sims):
            simulated_items = create_random_items(n, p)
            simulated_pools = split_into_sublists(simulated_items, m)
            simulation_costs.append(calculate_cost(simulated_pools))

        # save the results
        test_result = {
            "m": m,
            "cost_total" : numpy.mean(simulation_costs),
            "cost_variance" : numpy.var(simulation_costs),
        }
        tests.append(test_result)

    # print the results
    for test_result in tests:
        print(tex(test_result["m"], test_result["cost_total"], test_result["cost_variance"]))

# create an array of booleans, approximately p of which are False (defective) 
def create_random_items(n, p):
    arr = []
    for i in range(n):
        num = random.randint(1,int(1/p))
        arr.append( False if num == 1 else True)
    return arr 

# convert a list into a list of lists segmented into chunks 
def split_into_sublists(arr, size):
    a = [arr[x:x+size] for x in range(0, len(arr), size)]
    if not all(len(i) == len(a[0]) for i in a):
        return None 
    return a  

# check if all items in an list are True
def all_true(arr):
    return len(arr) == arr.count(True)

def calculate_cost(pools):
    cost = 0
    for pool in pools:
        # cost for initial test of pool
        cost += T
        # if all in pool are true, then only this one test needed to be conducted
        # otherwise, conduct tests again for all members of the pool
        if not all_true(pool): cost += len(pool)*T
    return cost 

# scatter plot a 2d array
def scatter(arr, connect_dots=False):
    colors = ["b", "r", "g", "y"]
    x = [i[0] for i in arr]
    for series in range(1, len(arr[0])):
        y = [i[series] for i in arr]
        plt.scatter(x, y, label=str(series), c=colors[series-1])
        if connect_dots: 
            plt.plot(x, y, label=str(series), c=colors[series-1])
    plt.legend()
    plt.show()

# format for easy copy-paste into LaTeX table
def tex(*args, dec=3):
    formatting = "%." + str(dec) + "f"
    l = [formatting % i for i in args]
    s = "\t&\t".join(l) + "\t\\\\"
    s = s.replace("." + "0" * dec ,"")
    return s

if __name__ == "__main__":
    main()

# OUTPUT
r"""
1	&	10	&	1000	&	5005	&	0	&	50050	&	0	\\
2	&	20	&	500	&	2504.999	&	2.820	&	50099.977	&	56.396	\\
3	&	50	&	200	&	1002.104	&	2887.190	&	50105.221	&	144359.508	\\
4	&	100	&	100	&	478.095	&	12728.742	&	47809.473	&	1272874.208	\\
5	&	200	&	50	&	197.007	&	11135.028	&	39401.450	&	2227005.660	\\
6	&	400	&	25	&	69.796	&	3900.979	&	27918.316	&	1560391.738	\\
7	&	500	&	20	&	49.259	&	2467.043	&	24629.582	&	1233521.403	\\
8	&	1000	&	10	&	17.670	&	472.974	&	17670.107	&	472973.746	\\
9	&	1250	&	8	&	13.339	&	264.013	&	16673.317	&	330016.246	\\
10	&	2000	&	5	&	8.399	&	73.413	&	16797.053	&	146826.359	\\
"""
