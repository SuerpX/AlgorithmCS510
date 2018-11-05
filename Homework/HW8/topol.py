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

def orderDFS(n, a):
    graph = {0:[]}
    s = [i for i in range(n)]

    for i in range(n):
        graph[i] = []
    for x, y in a:
        graph[y].append(x)

    def DFS(node):
        visited.append(node)
        for eachNode in graph[node]:
            if eachNode not in res and eachNode not in visited:
                DFS(eachNode)
            if eachNode in visited and eachNode not in res:
                return False
        res.append(node)
        return True
    res = []
    for node in s:
        visited = []
        if node not in res:
            if not DFS(node):
                return None
        
    return res
    



print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
print(order(4, [(0,1), (1,2), (2,1), (2,3)]))

print(orderDFS(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
print(orderDFS(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
print(orderDFS(4, [(0,1), (1,2), (2,1), (2,3)]))
