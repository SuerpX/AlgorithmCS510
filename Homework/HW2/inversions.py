def num_inversions(a):
    return inversions(a)[1]
def inversions(a):
    length = len(a)
    inversion = 0
    if length == 1:
        return [a[0]], 0
    leftA = [ ]
    rightA = [ ]
    mergeA = [ ]
    leftA +=  a[:length // 2]
    rightA += a[length // 2:]

    leftA, inver = inversions(leftA)
    inversion += inver
    rightA, inver = inversions(rightA)
    inversion += inver
    
    i = 0
    j = 0
    
    lengthL = length // 2
    lengthR = (length + 1) // 2
    while True:
        if leftA[i] < rightA[j]:
            mergeA.append(leftA[i])
            i += 1
            inversion += j
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
                inversion += j
            else:
                break
    return mergeA, inversion

#print(num_inversions([2, 4, 1, 3]))
