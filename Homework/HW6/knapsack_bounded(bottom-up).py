'''
from copy import *
def best(w, items):
    bagsOpt = {0 : 0}
    usedItem = {0 : 0}
    bestw = _best(w, items, usedItem, bagsOpt)
    s = []
    for i in usedItem:
        s.append(usedItem[i])
    return (bestw, s)
    
def _best(w, items, usedItem, bagsOpt):
    if w not in bagsOpt:
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
            vi = _best(w - i[0], items, ui, bagsOpt) + i[1]
            #print(w, usedItem)
            if maxV < vi:
                maxV = vi
                maxK = k
        if putted:
            bagsOpt[w] = maxV
            usedItem[maxK] += 1
        else:
            bagsOpt[w] = 0
        #print(w,maxK)
    print(usedItem)
    print(bagsOpt)
    return bagsOpt[w]
'''
def best(W, item):
    opt = [[0 for i in range(0, W + 1)] for j in range(0, len(item) + 1)]
    back = [[0 for i in range(0, W + 1)] for j in range(0, len(item) + 1)]

    for i, (w, v, c) in enumerate(item):
        i += 1
        for x in range(1, W + 1):
            for j in range(min(c, x // w) + 1):
                if x >= j * w and opt[i][x] < opt[i - 1][x - j * w] + j * v:
                    opt[i][x] = opt[i - 1][x - j * w] + j * v
                    back[i - 1][x] = j
    return opt[len(item)][W], tback(W, len(item) - 1,item, back)

def tback(w, i, item, back):
        if i < 0:
            return []
        new_w = w - item[i][0] * back[i][w]
        return tback(new_w, i - 1, item, back) + [back[i][w]]

#w = best(3, [(1, 5, 2), (1, 5, 3)])
#w = best(3, [(1, 4, 1), (1, 5, 3)])
#print(best(20, [ (2, 10, 3) , (3, 15, 4),(1, 10, 6)]))
#print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))
