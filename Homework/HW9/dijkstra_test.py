from collections import *
from heapdict import *
def shortest(n, a):
    edges = defaultdict(list)
    nodes = heapdict()
    back = defaultdict(int)
    for x in a:
        if x[0] not in edges:
            edges[x[0]] = []
        edges[x[0]].append((x[1], x[2]))
        edges[x[1]].append((x[0], x[2]))
 #       print(edges[x[0]])
    for i in range(n):
        nodes.__setitem__(i,float('inf'))
        back[i] = -1
    visited = []
    nodes.__setitem__(1760,0)
 #   print(edges, nodes)
    '''
    for x in range(n):
         print(edges[x])
    '''
    def _shortest(currentNode, v):
        
        visited.append(currentNode)
 #       print(currentNode)
        if currentNode == 669:
            return v
        for x in edges[currentNode]:
            if x[0] in visited:
                continue
            vn = v
            un = nodes.__getitem__(x[0])
 #           print(vn, un)
            if x[1] + vn < un:
                nodes.__setitem__(x[0], x[1] + vn)
                back[x[0]] = currentNode
 #               print(x[0], x[1] + vn)
 #       nodes.__delitem__(currentNode)
        nextNode, nextNodeV = nodes.popitem()
 #       print(nextNodeV)
        return _shortest(nextNode, nextNodeV)
    
    def traceback(currentNode):
        if currentNode == 1760:
            return [1760]
        return traceback(back[currentNode]) + [currentNode]
    
    nodes.popitem()
    optV = _shortest(1760,0)
    res = traceback(669)

    return (optV,res)

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
 #       print(shortest(2501, arr))
readFile('test1.txt')
#print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
