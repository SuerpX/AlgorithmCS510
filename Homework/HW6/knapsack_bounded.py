
def best(w, items):
    opt = {(0, 0) : 0}
    count = {(0,0) : 0}
    v = _best(w, items, len(items) - 1, opt, count)
 #   print(count)
    res = []
    for i in range(len(items) - 1, -1, -1):
        if w < 0:
            res.append(0)
            continue
        c = count[i, w]
        res.append(c)
        w -= c * items[i][0]
        
    res.reverse()
    return v, res
def _best(w, items, i, opt, count):
    if w <= 0 or i < 0:
        opt[i, w] = 0
        return opt[i, w]
    maxV = -1
    maxC = -1
    if (i, w) not in opt:
        wi, vi, ci = items[i]
        for c in range(0, ci + 1):
            if c * wi > w:
                break
            v = _best(w - (c * wi), items, i - 1, opt, count) + (c * vi)
            if v > maxV:
                maxV = v
                maxC = c
        if maxV >= 0:
            opt[i, w] = maxV
            count[i, w] = maxC


    return opt[i, w]
        

#w = best(3, [(1, 5, 2), (1, 5, 3)])
#w = best(3, [(1, 4, 1), (1, 5, 3)])
#print(best(20, [ (2, 10, 3) , (3, 15, 4),(1, 10, 6)]))
#print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))

#print(best(92, [(8, 9, 1000), (9, 10, 1000), (10, 12, 1000), (5, 6, 1000)]))
