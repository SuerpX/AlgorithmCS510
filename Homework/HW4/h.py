from random import *
from heapq import *
from timeit import *
from time import *

s = process_time()
for i in range(0,100):
    r = list(range(0,50000))
    reversed(r)
    heapify(r)

c = process_time() - s
print(c)

s = process_time()
for i in range(0,100):
    r = list(range(0,50000))
    h = []
    reversed(r)
    for j in r:
        heappush(h,j)

c = process_time() - s
print(c)
