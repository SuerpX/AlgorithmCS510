b = {0 : 1, 1 : 1}
def bst(n):
    if n not in b:
        sumN = 0
        for i in range(1, n + 1):
            if i - 1 not in b:
                s1 = bst(i - 1)
            else:
                s1 = b[i - 1]
            if n - i not in b:
                s2 = bst(n - i)
            else:
                s2 = b[n - i]
            sumN += s1 * s2
                
        b[n] = sumN
    return b[n]

print(bst(9))
