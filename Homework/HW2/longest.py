def longest(tree):
    a, b = _longest(tree)
    return a - 1

def _longest(tree):
    if tree == []:
        return 0, 0
    
    leftL, leftD = _longest(tree[0])
    rightL, rightD = _longest(tree[2])
    subL = Max(leftL, rightL)
    subD = Max(leftD, rightD)
    return Max(leftD + rightD, subL), subD + 1

def Max(a, b):
    return (a if a > b else b)
