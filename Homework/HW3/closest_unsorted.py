from random import randint
def find(a, num, k):
    b = []
    for x in a:
        b.append(abs(x - num))
        
    kthDifference = qselect(b, k)
    
    result = []
    x = 0
    smallerNum = 0
    for x in b:
        if x < kthDifference:
            smallerNum += 1
    sameNum = k - smallerNum
    i = 0
    for x in b:
        if x < kthDifference:
            result.append(a[i])
        if x == kthDifference and sameNum != 0:
            result.append(a[i])
            sameNum -= 1
        i += 1
    return result

def qselect(a, k):
    if len(a) == 1:
        return a[0]
    index = randint(0, len(a) - 1)
    a[index], a[0] = a[0], a[index]
    pivot = a[0]

    left = [x for x in a[1:] if x <= pivot]
    lengthL = len(left)

    if lengthL == k - 1:
        return pivot
    elif lengthL > k - 1:
        a[index], a[0] = a[0], a[index]
        return qselect(left, k)
    else:
        right = [x for x in a[1:] if x > pivot]
        a[index], a[0] = a[0], a[index]
        return qselect(right, k - len(left) - 1)

