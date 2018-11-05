import heapq
from random import randint

def nbesta(a,b):
    c = [(x,y) for x in a for y in b]
    c.sort(key = lambda k: (k[0] + k[1], k[1]))
    return c[:len(a)]

def qselect(i, a, key):
    if len(a) == 1:
        return a[0]
    r = randint(0,len(a) - 1)
    a[r], a[0] = a[0], a[r]
    pivot = a[0]
    smallers = [x for x in a[1:] if key(x) < key(pivot)]
    biggers = [x for x in a[1:] if key(x) >= key(pivot)]
    k = len(smallers) + 1
    if i == k:
        return a[0]
    elif i < k:
        return qselect(i, smallers, key)
    elif i > k:
        return qselect(i - k, biggers, key)
    
def nbestb(a,b):
    key = lambda k: (k[0] + k[1], k[1])
    c = [(x,y) for x in a for y in b]
    result = []
    for i in range (1, len(a) + 1):
        r = qselect(i, c ,key)
        result.append(r)
    return result

def nbestc(a,b):
    key = lambda k: (k[0] + k[1], k[1])
    if len(a) == []:
        return []
    l = len(a)
    res = []
    h = []
    usedPair = []
    
    sortedA = sorted(a)
    sortedB =  sorted(b)

    heapq.heappush(h, (key((sortedA[0], sortedB[0])), (0, 0)))
    while len(res) < l:
        i, j = heapq.heappop(h)[1]
        res.append((sortedA[i], sortedB[j]))
        
        if i + 1 < l and (i + 1, j) not in usedPair:
            heapq.heappush(h, (key((sortedA[ i + 1], sortedB[j])), (i + 1,j)))
            usedPair.append((i + 1, j))
        if j + 1 < l and (i, j + 1) not in usedPair:
            heapq.heappush(h, (key((sortedA[i], sortedB[j + 1])), (i,j + 1)))
            usedPair.append((i, j + 1))
            
    return res



def nbestC(a, b):
    sortedA = sorted(A)
    sortedB = sorted(B)

    h = []
    heapq.heappush(h, ((SortedA[0] + SortedB[0], SortedB[0]), (0, 0)))
    usedNodes = []
    usedNodes.append([0,0])
    res = []
    l = len(a)

    while len(res) < l:
        r = heapq.heappop(h)

        res.append([r[0][0] - r[0][1], r[0][1]])
        i, j = r[1]

        if i + 1 < l and [i + 1, j] not in usedNodes:
            heapq.heappush(h, ((SortedA[i + 1] + SortedB[j], SortedB[j]), (i + 1, j)))
            used
            

        






    


