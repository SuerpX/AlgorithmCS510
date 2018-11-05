from collections import *
#import collections
from heapdict import *
import sys
sys.setrecursionlimit(10000)

def shortest(n, a):
    edges = defaultdict(list)
    nodes = heapdict()
    back = defaultdict(int)
    for x in a:
        edges[x[0]].append((x[1], x[2]))
        edges[x[1]].append((x[0], x[2]))
        '''
    for i in range(n):
 #      nodes.__setitem__(i,float('inf'))
        back[i] = -1
        '''
    visited = set()
 #   nodes[0] = 0
    def _shortest(currentNode, v):
        
        visited.add(currentNode)
        if currentNode == n - 1:
            return v
        
        for un, volueOfun in edges[currentNode]:
            
            if un in visited:
                continue
            '''
            if x[0] not in nodes.__iter__():
                nodes.__setitem__(x[0], float('inf'))
            '''
            '''
            un = x[0]
            volueOfun = v + x[1]
            '''
            newvValueOfun = volueOfun + v
            '''
            un = nodes.__getitem__(x[0])
            '''
            
            if (un not in nodes.keys()) or (newvValueOfun < nodes[un]) :
                nodes[un] = newvValueOfun
                back[un] = currentNode
 #           print(nodes.__iter__())
        if len(nodes) == 0 :
            return None
        nextNode, nextNodeV = nodes.popitem()
        return _shortest(nextNode, nextNodeV)
    
    def traceback(currentNode):
        if currentNode == 0:
            return [0]
        return traceback(back[currentNode]) + [currentNode]
    
  #  t = nodes.popitem()
    optV = _shortest(0,0)
    if optV is None:
        return None

    return (optV,traceback(n - 1))

print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
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
'''
def doc(s):
    if hasattr(s, '__call__'):
        s = s.__doc__
    def f(g):
        g.__doc__ = s
        return g
    return f

class heapdict(collections.MutableMapping):
    __marker = object()

    @staticmethod
    def _parent(i):
        return ((i - 1) >> 1)

    @staticmethod
    def _left(i):
        return ((i << 1) + 1)

    @staticmethod
    def _right(i):
        return ((i+1) << 1)    
    
    def __init__(self, *args, **kw):
        self.heap = []
        self.d = {}
        self.update(*args, **kw)

    @doc(dict.clear)
    def clear(self):
        self.heap.clear()
        self.d.clear()

    @doc(dict.__setitem__)
    def __setitem__(self, key, value):
        if key in self.d:
            self.pop(key)
        wrapper = [value, key, len(self)]
        self.d[key] = wrapper
        self.heap.append(wrapper)
        self._decrease_key(len(self.heap)-1)

    def myDresaseKey(self, key, value):
        if key not in self.d:
            self.__setitem(key, value)
        else:
            self.d[key][0] = value
            self.heap[self.d[key][2]][0] = value
            self._decrease_key(self.d[key][2])

    def _min_heapify(self, i):
        l = self._left(i)
        r = self._right(i)
        n = len(self.heap)
        if l < n and self.heap[l][0] < self.heap[i][0]:
            low = l
        else:
            low = i
        if r < n and self.heap[r][0] < self.heap[low][0]:
            low = r

        if low != i:
            self._swap(i, low)
            self._min_heapify(low)

    def _decrease_key(self, i):
        while i:
            parent = self._parent(i)
            if self.heap[parent][0] < self.heap[i][0]: break
            self._swap(i, parent)
            i = parent

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.heap[i][2] = i
        self.heap[j][2] = j

    @doc(dict.__delitem__)
    def __delitem__(self, key):
        wrapper = self.d[key]
        while wrapper[2]:
            parentpos = self._parent(wrapper[2])
            parent = self.heap[parentpos]
            self._swap(wrapper[2], parent[2])
        self.popitem()

    @doc(dict.__getitem__)
    def __getitem__(self, key):
        return self.d[key][0]

    @doc(dict.__iter__)
    def __iter__(self):
        return iter(self.d)

    def popitem(self):
        """D.popitem() -> (k, v), remove and return the (key, value) pair with lowest\nvalue; but raise KeyError if D is empty."""
        wrapper = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
        else:
            self.heap[0] = self.heap.pop(-1)
            self.heap[0][2] = 0
            self._min_heapify(0)
        del self.d[wrapper[1]]
        return wrapper[1], wrapper[0]    

    @doc(dict.__len__)
    def __len__(self):
        return len(self.d)

    def peekitem(self):
        """D.peekitem() -> (k, v), return the (key, value) pair with lowest value;\n but raise KeyError if D is empty."""
        return (self.heap[0][1], self.heap[0][0])

del doc
__all__ = ['heapdict']
'''

