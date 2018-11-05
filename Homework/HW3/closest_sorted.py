import bisect
def find(a, num, k):
    index = bisect.bisect(a, num)
    pointLeft, pointRight = _find(a, num, k)
    
'''
    pointLeft = index - 1
    pointRight = index

    while k > 0:
        if pointRight >= len(a) or pointLeft >= 0 and num - a[pointLeft] <= a[pointRight] - num :
            pointLeft -= 1
        else:
            pointRight += 1
        k -= 1
'''
    return a[pointLeft + 1:pointRight]

def _find(a, pointLeft, pointRight, num, k):
    if k == 0:
        return 0,0
    if pointLeft >= 0 and num - a[pointLeft] <= a[pointRight] - num :
        return _find(a, num, k - 1)
    elif pointRight < len(a):
        return _find(a, num, k - 1)
