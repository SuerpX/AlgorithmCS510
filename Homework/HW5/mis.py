
def max_wis2(a):
    f = {-2 : 0, -1 : 0}
    trace = {-1: False}
    maxSet = _max_mis(a, f, len(a) - 1, trace)
    res = []
    i = len(a) - 1
#    print(trace)
    while i >= 0:
        if trace[i]:
            res.append(a[i])
            i -= 2
        else:
            i -= 1
    res.reverse()
    return (maxSet,res)

def _max_mis(a, f, n, trace):
    if n not in f:
        f1 = _max_mis(a, f, n - 1, trace)
        f2 = _max_mis(a, f, n - 2, trace) + a[n]
        f[n] = max(f1, f2)
        if f[n] == f1:
            trace[n] = False
        else:
            trace[n] = True
        
    return f[n]

def max_wis(a):
    trace = {-1: False}
    l = len(a)
    maxSet = 0
    b = 0
    c = 0
    res = []
    for i in range(0, l):
        b, c = c, max(c, b + a[i])
        if b == c:
            trace[i] = False
        else:
            trace[i] = True
    i = l - 1
    while i >= 0:
        if trace[i]:
            res.append(a[i])
            i -= 2
        else:
            i -= 1
    res.reverse()
    
    return c, res
    
'''
print(max_wis([7,8,5]))
print(max_wis([-1,8,10]))
print(max_wis([]))
'''
