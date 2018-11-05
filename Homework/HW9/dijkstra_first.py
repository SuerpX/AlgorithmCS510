from collections import *
import sys
sys.setrecursionlimit(10000)
class myHeapDict():
    def __init__(self):
        self.h = []
        self.d = defaultdict(int)
        self.len = 0
    def bubbleUp(self, n):
 #       print(n)
        while n > 0:
            parent = (n - 1) // 2
 #           print(self.h[parent],self.h[n])
            if self.h[parent] <= self.h[n]:
                return
            self.swap(parent, n)
            n = parent
        return
    def bubbleDown(self, n):
        left, right = n * 2 + 1, n * 2 + 2
        while right < self.len:
            minV = min(self.h[left], self.h[right], self.h[n])
            if minV == self.h[n]:
                return
            elif minV == self.h[left]:
                self.swap(left, n)
                n = left
            elif minV == self.h[right]:
                self.swap(right,n)
                n = right
            left, right = n * 2 + 1, n * 2 + 2
            
        if left < self.len:
            if self.h[left] < self.h[n]:
                self.swap(left, n)
    def push(self, key, value):
        l = len(self.h)
        self.h.append((value, key))
        self.d[key] = self.len
        self.bubbleUp(self.len)
        self.len += 1
 #       print(self.h, self.d)
    def popitem(self):
        if self.len == 0:
            return None
        
        self.swap(self.len - 1, 0)
        t = self.h.pop()
        self.len -= 1

        self.bubbleDown(0)
   #     print(t, self.h)
        return t
    def swap (self, i, j):
            self.h[i], self.h[j] = self.h[j], self.h[i]
            self.d[self.h[i][1]] = i
            self.d[self.h[j][1]] = j
    def deacreseKey(self, key, value):
 #      print(self.h)
        position = self.d[key]
        self.h[position] = (value,self.h[position][1])
        self.bubbleUp(position)
 #       print(self.h)
        
    def keys(self):
        return self.d
    def getitem(self, key):
 #       print(key)
 #       print(self.d,self.h)
        return self.h[self.d[key]][0]

def shortest(n, a):
    edges = defaultdict(list)
    nodes = myHeapDict()
    back = defaultdict(int)
    for x in a:
        edges[x[0]].append((x[1], x[2]))
        edges[x[1]].append((x[0], x[2]))
    visited = set()
    def _shortest(currentNode, v):
        visited.add(currentNode)
        if currentNode == n - 1:
            return v
        
        for un, volueOfun in edges[currentNode]:
            
            if un in visited:
                continue
            newvValueOfun = volueOfun + v
            
            if un not in nodes.keys():
                nodes.push(un, newvValueOfun)
                back[un] = currentNode
            elif newvValueOfun < nodes.getitem(un):
                nodes.deacreseKey(un, newvValueOfun)
                back[un] = currentNode
        if nodes.len == 0 :
            return None
        
        nextNodeV, nextNode = nodes.popitem()
        return _shortest(nextNode, nextNodeV)
    
    def traceback(currentNode):
        if currentNode == 0:
            return [0]
        return traceback(back[currentNode]) + [currentNode]
    
    optV = _shortest(0,0)
    if optV is None:
        return None

    return (optV,traceback(n - 1))

#print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
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
