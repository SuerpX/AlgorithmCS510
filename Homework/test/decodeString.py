decN = {0: 1, 1: 1}
def solveString(a):
    l = len(a)
    if l not in decN:
        decN[l] = solveString(a[1:])
        
        if len(a) > 1:
            if int(a[0]) * 10 + int(a[1]) <= 26 :
                decN[l] += solveString(a[2:])
    return decN[l]
        
print(solveString("12317212453214578123727172735"))
