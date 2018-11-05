from collections import *

class myHeapDict():
    def __init__(self):
        self.h = [] # heap
        self.d = defaultdict(int) # hash
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
 #       print(t, self.h)
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
        return self.h[self.d[key]][0]
'''
d = myHeapDict()
d.push('a',6)
d.push('b',2)
d.push('c',1)
d.push('d',8)
d.push('e',3)

d.popitem()
d.popitem()
d.popitem()
d.popitem()
d.popitem()
d.popitem()
'''
'''
d.deacreseKey(0.2,'c')
d.popitem()
'''


