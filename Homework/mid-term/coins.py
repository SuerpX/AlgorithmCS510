def stype(X, coins):
    back = {(0,0):0}
    opt = {(0,1) : 0}
    l = len(coins)
    for i in range(l + 1):
        opt[0, i] = 0
    t = 0
    def _stype(x, t):
        if x > 0 and t >= l:
            opt[x,t] = float('inf')
            return opt[x,t]
        if (x,t) in opt:
            return opt[x,t]

        minV = float('inf')
        minC = -1
        for j in range(100000):
            if j == 0:
                v = _stype(x, t + 1)
            elif x - j * coins[t] >= 0:
                v = _stype(x - j * coins[t], t + 1) + 1
                
            else:
                break
            
            if v < minV:
                
                minV = v
                minC = j
                '''
                if x - j * coins[t] == 0:
                    print("v:" + str(v))
                    print("minV:" + str(minV))
                '''
        opt[x,t] = minV
        back[x,t] = minC
        if minC == -1:
            back[x,t] = 0
        return opt[x,t]
    num = _stype(X, 0)
    res = []
    for i in range(0,len(coins)):
        if X < 0:
            res.append(0)
            continue
        c = back[X,i]
        res.append(c)
        X -= c * coins[i]
    print(num, res)

stype(6, [1,2,3])
stype(17, [2,3,5])
stype(103, [29,14,5,18])
