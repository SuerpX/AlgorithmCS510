from random import randint
def ksmallest(k, a):
    smallestHeap = []
    for x in a:
        if len(smallestHeap) < k:
            push(smallestHeap, x)
        elif smallestHeap[0] > x:
            replace(smallestHeap,x)
    smallestHeap = qsort(smallestHeap)
 #   smallestHeap = sorted(smallestHeap)
    return smallestHeap

def push(h, x):
    h.append(x)
    i = len(h) - 1

    while not i == 0:
        parent = (i - 1) // 2
        if h[parent] < h[i]:
            h[parent], h[i] = h[i], h[parent]
            i = parent
        else:
             break

def replace(h,x):
    h[0] = x
    i = 0
    while i * 2 + 1 < len(h):
        left = i * 2 + 1
        
        if i * 2 + 2 < len(h):
            right = i * 2 + 2
        maxX = max(h[i], h[left], h[right])
        if maxX == h[i]:
            break
        elif maxX == h[left]:
            switch = left
        elif maxX == h[right]:
            switch = right
        h[i], h[switch] = h[switch], h[i]
        i, switch = switch, i

def qsort(a):
    if a == []:
        return []
    else:
        '''
        index = randint(0,len(a) - 1)
        a[0], a[index] = a[index], a[0]
        '''
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return qsort(left) + [pivot] + qsort(right)

print(ksmallest(20, [10, 7, 23, 2, 9, 3, 7, 8, 11, 5, 7]))

print(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))

