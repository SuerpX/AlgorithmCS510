import sys

def max_wis(a):
    n = len(a)
    opt= {}
    for i in range(0,n):
        opt[i] = (-100000,False)
    opt[-2] = opt[-1] = (0,False)
    res = _max_wis(a,opt,n-1)
    #print opt
    return (res,trace(a,opt))



def _max_wis(a,opt,n):
    if opt[n][0] == -100000:
        pick = _max_wis(a,opt,n-2) + a[n]
        nopick = _max_wis(a,opt,n-1)
        opt[n] = (pick,True) if pick > nopick else (nopick,False)
        return opt[n][0]
    else:
        return opt[n][0]


def trace(a,opt,s =None):
    if s ==None:
        s = []
    i = len(a)-1
    while i >=0:
        if opt[i][1] == True:
            s.append(a[i]) 
            i-=2
        else:
            i-=1
    return s

def max_wis2(a,s=None):
    if s == None:
        s = []
    opt = {-1:0,-2:0}
    n=len(a)
    for i in xrange(0,n):
        opt[i] = max(a[i] + opt[i-2],opt[i-1])
    i = n-1
    while i >=0:
        if opt[i]>opt[i-1]:
            s.append(a[i])
            i-=2
        else:
            i-=1
    return opt[n-1],s

print(max_wis([7,8,5]))

