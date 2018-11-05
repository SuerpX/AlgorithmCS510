#!/usr/bin/env python3

from collections import defaultdict
import time
from heapdict import heapdict # SLOW
from priority_dict import priority_dict # FAST
from heapq import heappush, heappop

def tsp(n, _edges): # the Viterbi implementation

    def backtrace(i, nodeset, j):
        if j == 0:
            return [0]
        _, last = best[i][nodeset, j]
        newset = nodeset - frozenset([j])
        return backtrace(i-1, newset, last) + [j%n]

    start_time = time.time()

    edges = defaultdict(lambda : defaultdict(lambda : float("inf")))
    for (u,v,c) in _edges:
        edges[u][v] = min(edges[u][v], c) # possible duplicate edges
        edges[v][u] = min(edges[v][u], c) # undirected
    for u in range(1,n): # clone a special sink n from 0
        edges[u][n] = edges[u][0] 
        
    best = [defaultdict(lambda : (float("inf"), None)) for _ in range(n+2)] # best and back together
    
    best[1][frozenset([0]), 0] = (0, None)
    
    pushes = 0
    for i in range(1,n+1): #i->i+1
        for (nodeset, last), (value, _) in best[i].items():
        #for nodeset, last in best[i]:
            #value = best[i][nodeset, last]
            for j in range(1,n) if i < n else [n]:
                if j in edges[last] and j not in nodeset:
                    newvalue = value + edges[last][j]
 #                   print(nodeset)
                    newset = nodeset | frozenset([j])
#                    print(newset)
                    if newvalue < best[i+1][newset, j][0]:
                        pushes += 1
                        best[i+1][newset, j] = (newvalue, last)
 #   print(best)
    fullsetplus = frozenset(range(n+1)) # Matthew's suggestion
            
    print("Viterbi, set, time: %.2f" % (time.time() - start_time), "pushes:", pushes)
    return (best[n+1][fullsetplus, n][0], backtrace(n+1, fullsetplus, n))    

def tsp_bit(n, _edges): # the Viterbi implementation

    def backtrace(i, nodeset, j):
        if j == 0:
            return [0]
        _, last = best[i][nodeset, j]
        return backtrace(i-1, nodeset - (1 << j), last) + [j%n] # last one should be 0

    start_time = time.time()

    edges = defaultdict(lambda : defaultdict(lambda : float("inf")))
    for (u,v,c) in _edges:
        edges[u][v] = min(edges[u][v], c) # possible duplicate edges
        edges[v][u] = min(edges[v][u], c) # undirected
    for u in range(1,n): # Matthew's suggestion: clone a special sink n from 0
        edges[u][n] = edges[u][0] 
        
    best = [defaultdict(lambda : (float("inf"), None)) for _ in range(n+2)] # best and back together
    best[1][1, 0] = (0, None) # 1: 000001
    pushes = 0
    for i in range(1,n+1): #i->i+1
        for (nodeset, last), (value, _) in best[i].items():
        #for nodeset, last in best[i]:
            #value = best[i][nodeset, last]
            for j in range(1,n) if i < n else [n]:
                if j in edges[last] and not (1<<j & nodeset):
                    newvalue = value + edges[last][j]
                    newset = nodeset | (1<<j)
                    
                    if newvalue < best[i+1][newset, j][0]:
                        pushes += 1
                        best[i+1][newset, j] = (newvalue, last)

    fullsetplus = 2**(n+1) - 1 #frozenset(range(n+1)) 111...1
            
    print("Viterbi, bit, time: %.2f" % (time.time() - start_time), "pushes:", pushes)
    return (best[n+1][fullsetplus, n][0], backtrace(n+1, fullsetplus, n))

def tsp_dijk_bit_pqdict(n, _edges): # the Dijkstra implementation

    def backtrace(nodeset, j):
        if nodeset == 1:
            return [0]
        last = fixed[nodeset, j]
        return backtrace(nodeset - (1<<j), last) + [j%n]

    start_time = time.time()

    edges = defaultdict(lambda : defaultdict(lambda : float("inf")))
    for (u,v,c) in _edges:
        edges[u][v] = min(edges[u][v], c) # possible duplicate edges
        edges[v][u] = min(edges[v][u], c) # undirected
    for u in range(1,n): # Matthew's suggestion: clone a special sink n from 0
        edges[u][n] = edges[u][0] 
        
    queue = priority_dict() #heapdict()
    queue[1, 0] = (0, -1)
    fixed = {}

    pushes = pops = 0
    full, fullplus = 2**n-1, 2**(n+1)-1
    while queue:
        (nodeset, last), (value, back) = queue.popitem()
        pops += 1
        fixed[nodeset, last] = back
        if nodeset == fullplus: # full set + [0]
            print("Dijkstra, bit, pqdict, time: %.2f" % (time.time() - start_time), "pushes:", pushes, "pops:", pops)
            return (value, backtrace(nodeset, last))    
            
        for j in range(1,n) if nodeset < full else [n]:
            if j in edges[last] and not (1<<j & nodeset):
                newvalue = value + edges[last][j]
                newset = nodeset | (1<<j)
                if (newset, j) not in fixed and \
                   ((newset, j) not in queue or newvalue < queue[newset, j][0]):
                    #print("push", newvalue, newset, j)
                    queue[newset, j] = (newvalue, last)
                    pushes += 1

def tsp_dijk_bit_heapq(n, _edges): # the Dijkstra implementation

    def backtrace(nodeset, j):
        if nodeset == 1:
            return [0]
        last = fixed[nodeset, j]
        return backtrace(nodeset - (1<<j), last) + [j%n]

    start_time = time.time()

    edges = defaultdict(lambda : defaultdict(lambda : float("inf")))
    for (u,v,c) in _edges:
        edges[u][v] = min(edges[u][v], c) # possible duplicate edges
        edges[v][u] = min(edges[v][u], c) # undirected
    for u in range(1,n): # Matthew's suggestion: clone a special sink n from 0
        edges[u][n] = edges[u][0] 
        
    queue = [(0, (1, 0), None)] # (value, (nodeset, last), back)
    fixed = {}

    pushes = pops = 0
    full, fullplus = 2**n-1, 2**(n+1)-1
    while queue != []:
        value, (nodeset, last), back = heappop(queue)
        pops += 1
        if (nodeset, last) not in fixed:
            fixed[nodeset, last] = back
            if nodeset == fullplus: # full set + [0]
                print("Dijkstra, bit, heapq, time: %.2f" % (time.time() - start_time), "pushes:", pushes, "pops:", pops)
                return (value, backtrace(nodeset, last))    

            for j in range(1,n) if nodeset < full else [n]:
                if j in edges[last] and not (1<<j & nodeset):
                    newvalue = value + edges[last][j]
                    newset = nodeset | (1<<j)
                    if (newset, j) not in fixed: # and newvalue < best[newset, j]:
                        heappush(queue, (newvalue, (newset, j), last))
                        pushes += 1


if __name__ == "__main__":
    
    print (tsp_bit(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
    print (tsp_bit(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6), (3,0,1)]))
    # print (tsp_dijk(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6), (3,0,1)]))
    # map of germany: https://stackoverflow.com/questions/11007355/data-for-simple-tsp # dense graph!
    germany = [(0,1,29),(0,2,20),(0,3,21),(0,4,16),(0,5,31),(0,6,100),(0,7,12),(0,8,4),(0,9,31),(0,10,18), 
               (1,2,15),(1,3,29),(1,4,28),(1,5,40),(1,6,72),(1,7,21),(1,8,29),(1,9,41),(1,10,12),
               (2,3,15),(2,4,14),(2,5,25),(2,6,81),(2,7,9),(2,8,23),(2,9,27),(2,10,13),
               (3,4,4),(3,5,12),(3,6,92),(3,7,12),(3,8,25),(3,9,13),(3,10,25),
               (4,5,16),(4,6,94),(4,7,9),(4,8,20),(4,9,16),(4,10,22),
               (5,6,95),(5,7,24),(5,8,36),(5,9,3),(5,10,37),
               (6,7,90),(6,8,101),(6,9,99),(6,10,84),
               (7,8,15),(7,9,25),(7,10,13),
               (8,9,35),(8,10,18),
               (9,10,38)]
    print (tsp_bit  (11, germany))
    print (tsp_dijk_bit_pqdict (11, germany))
    print (tsp_dijk_bit_heapq (11, germany))

    import random
    random.seed(2)
    n, m = 16, 100
    edges = [(random.randint(0,n-1), random.randint(0,n-1), random.randint(0,5)) for _ in range(m)] + \
            [(random.randint(0,n-1), random.randint(0,n-1), random.randint(6,10)) for _ in range(m)] 
    #print (edges)
    
    print (tsp (4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])) # (11, [0, 4, 1, 3, 2, 0])
 #   print (tsp_bit (n, edges)) # (11, [0, 4, 1, 3, 2, 0])

    print (tsp_dijk_bit_pqdict (n, edges))
    print (tsp_dijk_bit_heapq (n, edges))
