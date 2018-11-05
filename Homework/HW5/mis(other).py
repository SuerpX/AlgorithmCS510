
def max_wis(a):
    mw = {-2 : 0, -1 : 0}
    path = {-2 : False, -1 : False}
    for i in range(0, len(a)):
        path[i] = False
    maxN = _max_wis(len(a) - 1, a, mw, path)
    p = []
    i = len(a) - 1
    while i >= 0:
        if path[i]:
           p.append(a[i])
           i -= 2
        else:
            i -= 1
            
    p.reverse()
    return (maxN, p)


def _max_wis(n, a, mw, path):
    if n not in mw:
         if a[n] > 0:
             n1 = _max_wis(n - 1, a, mw, path)
             n2 = _max_wis(n - 2, a, mw, path) + a[n]
             if n1 > n2:
                 mw[n] = n1
                 path[n] = False
             else:
                 mw[n] = n2
                 path[n] = True
         else:
            mw[n] = _max_wis(n - 1, a, mw, path)
            path[n] = False
    print(mw[n])
    return mw[n]

def max_wis2(a):
    mw = {-2 : 0, -1 : 0}
    for i in range(0, len(a)):
        mw[i] = max(mw[i - 1], mw[i - 2] + a[i])
        
    p = []
    i = len(a) - 1
    while i >= 0:
        if mw[i] > mw[i - 1]:
           p.append(a[i])
           i -= 2
        else:
            i -= 1
            
    p.reverse()
    return (mw[len(a) - 1], p)


print(max_wis([7,8,5]))
print(max_wis([-1,8,10]))
print(max_wis([]))
