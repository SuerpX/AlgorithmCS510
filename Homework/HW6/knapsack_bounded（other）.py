'''
from copy import *
def best(w, items):
    bagsdp = {0 : 0}
    usedItem = {0 : 0}
    bestw = _best(w, items, usedItem, bagsdp)
    s = []
    for i in usedItem:
        s.append(usedItem[i])
    return (bestw, s)
    
def _best(w, items, usedItem, bagsdp):
    if w not in bagsdp:
        maxV = 0
        maxK = 0
        putted = False
        for k, i in enumerate(items):
            if k not in usedItem:
                usedItem[k] = 0
            if i[2] <= usedItem[k] or w < i[0]:
                continue

            putted = True
            ui = deepcopy(usedItem)
            ui[k] += 1
            #print(ui)
            #print(w, usedItem)
            vi = _best(w - i[0], items, ui, bagsdp) + i[1]
            #print(w, usedItem)
            if maxV < vi:
                maxV = vi
                maxK = k
        if putted:
            bagsdp[w] = maxV
            usedItem[maxK] += 1
        else:
            bagsdp[w] = 0
        #print(w,maxK)
    print(usedItem)
    print(bagsdp)
    return bagsdp[w]
'''
from collections import *
def best_bottomUp(W, items):
    
    count = defaultdict(int)
    dp = {(0,0) : 0}
    for w in range(1, W+1):
        for x, item in enumerate(items):
            wi, vi, ci = item
            for c in range(ci+1):
                if w - wi * c < 0:
                    break
                ans = dp[w - wi * c, x - 1] + vi * c
                if ans > dp[w, x]:
                    dp[w, x] = ans
                    count[w, x] = c
    return dp[W,len(items)-1], backtrack(W, items, count)
def backtrack(w, items, count):
    result = []
    i = w
    for x in range(len(items)-1, -1, -1):
        c = count[i,x]
        result.append(c)
        wi = items[x][0]
        i -= wi*c
    list.reverse(result)
    return result

def best(W, items):
    dp = defaultdict(int)
    count = defaultdict(int)

    res = _best(W, len(items)-1, items, dp, count)
    return res, backtrack(W, items, count)

def _best(w, i, items, dp, count):

    if w <= 0 or i < 0:
        return 0
    if dp[w, i] != 0:
        return dp[w,i]

    wi, vi, ci = items[i]
    maxCopy = 0
    for c in range(ci+1):
        if w - wi * c < 0:
            break
        v = _best(w - wi * c, i-1, items, dp, count) + vi * c
        if dp[w, i] < v:
                dp[w, i] = v
                maxCopy = c
    count[w,i] = maxCopy
    return dp[w,i]

#w = best(3, [(1, 5, 2), (1, 5, 3)])
#w = best(3, [(1, 4, 1), (1, 5, 3)])
#print(best(20, [ (2, 10, 3) , (3, 15, 4),(1, 10, 6)]))
print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))

#print(best(92, [(8, 9, 1000), (9, 10, 1000), (10, 12, 1000), (5, 6, 1000)]))
