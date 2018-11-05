from heapq import merge
def kmergesort(a, k):
    sortedA = []
    l = len(a)
    if l <= 1:
        return a
    partN = (l - 1) // k + 1

    for i in range(0, l, partN):
        sortedA.append(kmergesort(a[i: i + partN],k))

    return list(merge(*sortedA))]
        
        

print(kmergesort([4,1,5,2,6,3,7,0], 5))
