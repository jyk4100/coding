## leetcode 743 Network Delay Time
## jyk4100
## last modified: 2021-05-28
## https://leetcode.com/problems/network-delay-time/

## function
def networkmax(times, n, k):
    d = [-999] + [999 for x in range(0,n)]
    d[k] = 0
    re = set() ## "reachable edges"
    re.add(k)
    for j in range(0, n):
        ## print("bf iteration {}".format(j)) ## ouptut limit;;
        for i in range(0,len(times)):
            u = times[i][0]
            v = times[i][1]
            w = times[i][2]
            re.add(v)
            ## edge relaxation
            if d[u] + w <= d[v]:
                ## print("edge ({},{}) relation".format(u,v))
                d[v] = d[u] + w
            ## else:
                ## print("no edge relaxation")
    if len(re) < n:
        print("cannot reach {} vertices".format(n))
        return(-1)
    else:
        return(max(d))
    
    
## we can use bellman-ford algorithm but how to put this edges in to graph representaion/class???
# import collections
# graph = collections.defaultdict(list)
# for u, v, w in times:
#     graph[u].append((v, w)) 
## nope don't like this "edge representation" essentially same
times = [[1,2,1]]
n = 2 ## total number of vertices
k = 2 ## source!!!
## okay assume we know there are 4 edges
## initialization
d = [-1] + [999 for x in range(0,n)]
## -999 because edge start from 1 to n
d[k] = 0
## re = set() ## reachable edges
## re.add(k)
for j in range(0, (len(times))):
    print("bf iteration {}".format(j))   
    for i in range(0,len(times)):
        u = times[i][0]
        v = times[i][1]
        w = times[i][2]
        ## add possible edges?
        ## re.add(v)
        ## edge relaxation
        if d[u] + w <= d[v]:
            print("edge ({},{}) relation".format(u,v))
            d[v] = d[u] + w
        else:
            print("no edge relaxation")
d
re
## if there is 999 that's not reachable so no need for the set