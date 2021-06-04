## leetcode 70 climbing stairs
## jyk4100
## last modified: 2021-06-04
## https://leetcode.com/problems/climbing-stairs/


# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

import math

[dpfibo(x) for x in range(3,20)]
[badfibo(x) for x in range(1,20)]



## zzz brute force 
def badfibo(n):
    # itr = math.floor(math.log(n, 2)) + 1
    itr = math.ceil(n/2)
    temp = 0
    for i in range(1, (itr)):
        temp = temp + math.comb(n-i, i)
        # print("{} chose {}".format(n-i, i))
        # print("temp {}".format(temp))
    temp = temp + 1 + (1 if n%2 == 0 else 0)
    return temp

## dynamic programming "recurion+memo bottom up"
fibMemo = [0, 1]
def dpfibo(n): 
    ## non negative integer
    # if n <= 0:
    #     print("Incorrect input")
    ## fib
    if n <= len(fibMemo):
        return fibMemo[n - 1]
    else:
        temp = dpfibo(n - 1) + dpfibo(n - 2)
        fibMemo.append(temp)
        return temp

## actual computation
# def nchooser(n, c):
#     temp = math.factorial(n)/math.factorial(c)/math.factorial(n-c)
#     return temp
## python math implementation? gamma function?
# nchooser(4,2)
# math.comb(4,2)
