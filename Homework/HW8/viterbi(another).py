def order(n, a):
    graph = {0:[]}
    count = {0:0}
    for i in range(n):
        graph[i] = []
        count[i] = 0
        
    for x, y in a:
        graph[x].append(y)
        count[y] += 1

    noPre = []
    res = []
    for i in range(n):
        if count[i] == 0:
            noPre.append(i)
    for x in noPre:
        res.append(x)
        for y in graph[x]:
            count[y] -= 1
            if count[y] == 0:
                noPre.append(y)
    if len(res) == n:
        return res
    else:
        return None
    
def orderDFS(n, a, graph = {0:[]}):

    for i in range(n):
        graph[i] = []
    for x, y in a:
        graph[y].append(x)

    def DFS(node):
        visited.add(node)
        eachVisited.add(node)
        for eachNode in graph[node]:
            if eachNode not in visited:
                if not DFS(eachNode):
                    return False
            if eachNode in eachVisited:
                return False
        eachVisited.remove(node)
        res.append(node)
        return True
    res = []
    visited = set()
    for node in range(n - 1,-1,-1):
        eachVisited = set()
        if  node not in visited:
            if not DFS(node):
                return None
        
    return res
    
def longest(n, a):
    graph = {0:[]}
    topo = orderDFS(n,a,graph)
    if topo is None:
        return None
    '''
    for i in range(n):
        graph[i] = []
    for x, y in a:
        graph[y].append(x)
    '''
    opt = {-1 : 0}
    back = {-1 : 0}
    def _longest(node):
        if node in opt:
            return opt[node]
        if len(graph[node]) == 0:
            opt[node] = 0
            return opt[node]
        maxL = -1
        maxJ = -1
        for j in graph[node]:
            l = _longest(j) + 1
            if l > maxL:
                maxL = l
                maxJ = j
        opt[node] = maxL
        back[node] = maxJ
        return opt[node]

    mL = -1
    mI = -1
    for i in range(n):
        if i not in opt:
            l = _longest(i)
            if mL < l:
                mL = l
                mI = i
 #   print(back)
    
    def traceBack(i):
        if i in back:
            return traceBack(back[i]) + [i]
        else:
            return [i]
    
    return (mL, traceBack(mI))
    

'''
print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
print(order(4, [(0,1), (1,2), (2,1), (2,3)]))
'''

print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
print(longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
print(longest(4, [(0,1), (1,2), (2,1), (2,3)]))

