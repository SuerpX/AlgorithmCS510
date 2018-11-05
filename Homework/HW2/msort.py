
def mergesort(a):
    length = len(a)
    if length == 1:
        return [a[0]]
    leftA = [ ]
    rightA = [ ]
    mergeA = [ ]
    leftA +=  a[:length // 2]
    rightA += a[length // 2:]

    leftA = mergesort(leftA)
    rightA = mergesort(rightA)
    
    i = 0
    j = 0
    
    lengthL = length // 2
    lengthR = (length + 1) // 2
    while True:
        if leftA[i] < rightA[j]:
            mergeA.append(leftA[i])
            i += 1
        else:
            mergeA.append(rightA[j])
            j += 1
        if i > lengthL - 1:
            break
        if j > lengthR - 1:
            break

    if i == lengthL:
        while True:
            if j < lengthR:
                mergeA.append(rightA[j])
                j += 1
            else:
                break
    if j == lengthR:
        while True:
            if i < lengthL:
                mergeA.append(leftA[i])
                i += 1
            else:
                break
    return mergeA

print(mergesort([4, 2, 5, 1, 6, 3]))
