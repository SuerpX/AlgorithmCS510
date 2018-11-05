from copy import *
opt = {0 : 0}
count = {-1: []}
def best(w, items, opt = None):
    if opt == None:
        opt = {0:0}
    count[0] = [0] * len(items)
    v, c = _best(w, items)
    
    return v, c

def _best(w, items):
    if w not in opt:
        maxV = -1
        maxI = -1
        maxC = []
        for i, k in enumerate(items):
            if k[0] <= w:
                v, c = _best(w - k[0], items)
                v +=  k[1]
                if v > maxV:
                    maxV = v
                    maxI = i
                    maxC = deepcopy(c)
            '''
            else:
                opt[w] = 0
                return opt[w]
            '''
        if maxI != -1:
            maxC[maxI] += 1
            count[w] = deepcopy(maxC)
            opt[w] = maxV
        else:
            opt[w] = 0
            count[w] = [0] * len(items)
    return opt[w], count[w]

#print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))
print(best(58, [(5, 9), (9, 18), (6, 12)]))
