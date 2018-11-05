from collections import defaultdict
import heapq
import sys
from random import randint

sys.setrecursionlimit(1000000)
pairs = frozenset(['AU', 'GC', 'GU', 'UA', 'CG', 'UG'])


def best(rna):
    return
def total(rna):
    return
def kbest(subrna,K, opt = defaultdict(list)):
    if subrna in opt:
       return opt[subrna]
    if len(subrna) == 1:
        opt[subrna] = [(0, '.')]
        return opt[subrna]
    elif len(subrna) == 0:
        opt[subrna] = [(0, '')]
        return opt[subrna]
    matrix = []
    h = []
    used = set()
    rnal = len(subrna)
    qselectarr = []
    
    matrixn = 0
    for k in range(1, rnal):
        #
        if subrna[0] + subrna[k] in pairs:               
             left = kbest(subrna[1:k],K)
             right = kbest(subrna[k + 1:],K)
             matrix.append((left,right))
             qselectarr.append(left[0][0] + right[0][0] + 1)
             matrixn += 1
             
    np = kbest(subrna[1:],K)
    qselectarr.append(np[0][0])
    matrix.append((np))


    def qselect(i, a):
        if len(a) == 1:
            return a[0]
        r = randint(0,len(a) - 1)
        a[r], a[0] = a[0], a[r]
        pivot = a[0]
        smallers = [x for x in a[1:] if x < pivot]
        k = len(smallers) + 1
        if i == k:
            return a[0]
        elif i < k:
            return qselect(i, smallers)
        elif i > k:
            biggers = [x for x in a[1:] if x >= pivot]
            return qselect(i - k, biggers)           
    if len(qselectarr) > K:
        kth = qselect(K, qselectarr)
        newMatrix = []
        newlength = 0
        for n, m in enumerate(matrix):
            if n != matrixn and m[0][0][0] + m[1][0][0] + 1 >= kth:
                newMatrix.append((m[0],m[1]))
                heapq.heappush(h,(-(m[0][0][0] + m[1][0][0] + 1), newlength,'(%s)' % m[0][0][1] + m[1][0][1] ,0 ,0))
                used.add((newlength , 0, 0))
                newlength += 1
            if n == matrixn and m[0][0] >= kth:
                newMatrix.append(m[0])
                heapq.heappush(h,(-(m[0][0]), newlength, '.%s' %  m[0][1],0 ,0))
                used.add((newlength,0,0))
                newlength += 1
                
        matrix = newMatrix
        matrixn = len(matrix) - 1
    else:
        for n, m in enumerate(matrix):
            if n != matrixn:
                heapq.heappush(h,(-(m[0][0][0] + m[1][0][0] + 1), n,'(%s)' % m[0][0][1] + m[1][0][1] ,0 ,0))
                used.add((n , 0, 0))
            else:
                heapq.heappush(h,(-(m[0][0]), n,  '.%s' %  m[0][1],0 ,0))
                used.add((n,0,0))

    
    res = []
    '''
    def put(k, i, j):
        if k == matrixn:
#                print(j)
#                np = _kbest(matrix[matrixn][0],matrix[matrixn][1])


#           else:
            #
   '''

    while len(res) < K and h != []:
        v, k, s, i, j = heapq.heappop(h)
        res.append((-v, s))
        if k == matrixn:
            i += 1
            if i < len(np) and (k, i,j) not in used:
                heapq.heappush(h, (-np[i][0], matrixn, '.%s' % np[i][1], i, 0))
                used.add((k, i, j))
        else:
            '''
            put(k, i + 1, j)
            put(k, i, j + 1)
            '''
            left = matrix[k][0]
            right = matrix[k][1]
            i += 1
            if (k, i, j) not in used and i < len(left)  and j < len(right):
                heapq.heappush(h, (-(left[i][0] + 1 + right[j][0]), k, '(%s)' % left[i][1] + right[j][1],i, j))
                used.add((k, i, j))
            i -= 1
            j +=1
            if (k, i, j) not in used and i < len(left)  and j < len(right):
                heapq.heappush(h, (-(left[i][0] + 1 + right[j][0]), k, '(%s)' % left[i][1]+right[j][1],i, j))
                used.add((k, i, j))
    opt[subrna] = res
    return opt[subrna]
#print(kbest("AGGCAUCAAACCCUGCAUGGGAGCG", 10))
