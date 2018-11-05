from collections import defaultdict
from heapdict1 import *

def shortest(n, a):
    edges = defaultdict(list)
    nodes = keyPQ([[0,0]])
    back = defaultdict(int)
    for x in a:
        if x[0] not in edges:
            edges[x[0]] = []
        edges[x[0]].append((x[1], x[2]))
        edges[x[1]].append((x[0], x[2]))
    for i in range(n):
 #      nodes.__setitem__(i,float('inf'))
        back[i] = -1
    visited = []
    def _shortest(currentNode, v):
        
        visited.append(currentNode)
        if currentNode == n - 1:
            return v
        for x in edges[currentNode]:
            if x[0] in visited:
                continue
            if x[0] not in nodes.__iter__():
                nodes.__setitem__(x[0], float('inf'))
            vn = v
            un = nodes.__getitem__(x[0])
            if x[1] + vn < un:
                nodes.myDresaseKey(x[0], x[1] + vn)
                back[x[0]] = currentNode
        nextNode, nextNodeV = nodes.popitem()
        return _shortest(nextNode, nextNodeV)
    
    def traceback(currentNode):
        if currentNode == 0:
            return [0]
        return traceback(back[currentNode]) + [currentNode]
    
    t = nodes.pop()
    print(t)
    optV = _shortest(t[1],t[0])
    res = traceback(n - 1)

    return (optV,res)

'''
def readFile(filename):
    
    file1 = open(filename,mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
    try:
        l = file1.readline( )
        l = file1.readline()
        arr = []
        while l:
            a,b,c =  l.split(' ')
            arr.append((int(a),int(b), int(c)))
 #           print(arr)
            l = file1.readline()
            
        
    finally:
        file1.close()
        print(shortest(2501, arr))
readFile('test1.txt')
'''
print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
