import heapq
from random import randint
def nbesta(arrA, arrB):
    a = sorted(arrA)
    b = sorted(arrB)
    print(a)
    print(b)
    l = len(arrA)
    i = 0
    j = 0
    h = []
    heapq.heappush(h, ((a[0] + b[0], a[0]),(0,0)))
    res =[]
    
    while len(res) < l:
        r = heapq.heappop(h)
        
        res.append([r[0][0] - r[0][1], r[0][1]])
        i, j = r[1]

        if i + 1 < l and ((a[i + 1] + b[j], b[j]),(i + 1, j)) not in h:
            i += 1
            heapq.heappush(h, ((a[i] + b[j], b[j]),(i, j)))
            i -= 1
        if j + 1 < l and ((a[i] + b[j + 1], b[j + 1]),(i, j + 1)) not in h:
            j += 1
            heapq.heappush(h, ((a[i] + b[j], b[j]),(i, j)))
            
        print(h)

    print(res)
        
nbesta([4, 1, 5, 3], [2, 6, 3, 4])
