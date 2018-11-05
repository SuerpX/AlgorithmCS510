from random import randint
def qselect(i, a):
    if len(a) == 1:
        return a[0]
    r = randint(0,len(a) - 1)
    a[r], a[0] = a[0], a[r]
    pivot = a[0]
    smallers = [x for x in a[1:] if x < pivot]
    biggers = [x for x in a[1:] if x >= pivot]
    k = len(smallers) + 1
    if i == k:
        return a[0]
    elif i < k:
        return qselect(i, smallers)
    elif i > k:
        return qselect(i - k, biggers)
