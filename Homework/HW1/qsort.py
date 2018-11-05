def sort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]

#tree = [[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]

def sorted(t):
    if t == []:
        return []
    return sorted(t[0]) + [t[1]] + sorted(t[2])

def search(t, x):
    if _search(t, x) == []:
        return False
    else:
        return True

def insert(t, x):
    p = _search(t,x)
    if p == []:
        p += [[], x, []]
        

def _search(t, x):
    if t == []:
        return t
    if t[1] == x:
        return t
    elif x < t[1]:
        return _search(t[0], x)
    elif x > t[1]:
        return _search(t[2], x)
    return t
 

        
    
