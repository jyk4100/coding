# python code for <>
# written on Fri May 28 23:43:48 2021 by @author: Kim Jungyoon


## leetcode 743 Network Delay Time
## jyk4100
## last modified: 2021-05-28

## https://leetcode.com/problems/network-delay-time/
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# You are given a network of n nodes, labeled from 1 to n.
# You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), 
# We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. 
# If it is impossible for all the n nodes to receive the signal, return -1.

## we can use bellman-ford algorithm but how to put this edges in to graph representaion/class???
# import collections
# graph = collections.defaultdict(list)
# for u, v, w in times:
#     graph[u].append((v, w)) 
## nope don't like this "edge representation"

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

## okay assume we know there are 4 edges

## initialization
d = [-999] + [999 for x in range(0,n)]
## -999 because edge start from 1 to n
d[k] = 0

for i in range(0,3):
    u = times[i][0]
    v = times[i][1]
    w = times[i][2]
    ## edge relaxation
    if d[u] + w <= d[v]:
        print("edge ({},{}) relation".format(u,v))
        d[v] = d[u] + w
    else:
        print("no edge relaxation")
    
# for i in range(0, len(times)):
#     print(times[i][2])




## i know not complete but submit
def networkmax(times, n, k):
    d = [-999] + [999 for x in range(0,n)]
    for i in range(0,len(times)):
        u = times[i][0]
        v = times[i][1]
        w = times[i][2]
        ## edge relaxation
        if d[u] + w <= d[v]:
            print("edge ({},{}) relation".format(u,v))
            d[v] = d[u] + w
        else:
            print("no edge relaxation")
    return(max(d))

networkmax(times=times, n=n, k=k)
