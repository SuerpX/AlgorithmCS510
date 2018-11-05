from collections import defaultdict
import heapq
import sys
from random import randint
import random

sys.setrecursionlimit(1000000)
pairs = frozenset(['AU', 'GC', 'GU', 'UA', 'CG', 'UG'])
def best(rna):
    opt = {(0,0):0}
    back = {(0,0):[0,0]}
    def _best(start,end):
        if end - start < 2:
           return 0
        if (start,end) in opt:
           return opt[start,end]
        bestV = -1
        back[start, end] = [None,None]
        #
        if rna[start] + rna[end - 1] in pairs:
            bestV = _best(start + 1, end - 1) + 1
            back[start,end][0] = [start + 1, end - 1]
        #
            
        for k in range(start + 1, end):
            v = _best(start,k) + _best(k,end)
            if v > bestV:
                bestV = v
                back[start,end][0] = [start,k]
                back[start,end][1] = [k,end]

                
        opt[start,end] = bestV
        return opt[start,end]
    
    bestn = _best(0, len(rna))
    res = ['.'] * len(rna)
    
    def traceback(s,e):
        if e - s < 2:
           return
        nonlocal res
        if back[s,e][1] is not None:
            i, j = back[s,e][0]
            traceback(i,j)
            i2, j2 = back[s,e][1]
            traceback(i2,j2)
        else:
            i, j = back[s,e][0]
            res[i - 1] = '('
            res[j] = ')'
            traceback(i,j)
    
    traceback(0,len(rna))
    res = "".join(res)
 #   print(opt)
    return bestn,res
'''
print(best("ACAGU"))
print(best("GUUAGAGUCU"))
print(best("AUAACCUUAUAGGGCUCUG"))
print(best("UUGGACUUGAGAAAAG"))
print(best("UCAAUGGGUAGUAAAU"))
print(best("CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU"))
print(best('CGAGGUGGCACUGACCAAACACCACCGAAAC'))
'''

def total(rna):
    opt = {(0,0):0}
    def _total(start,end):
        if end - start < 2:
           return 1
        if (start,end) in opt:
           return opt[start,end]
        bestV = 0
        
        for k in range(start + 1, end):
            if rna[start] + rna[k] in pairs:
                bestV += _total(start + 1,k) * _total(k + 1,end)
        bestV += _total(start + 1, end)
        opt[start,end] = bestV
        
 #       print(opt)
        return opt[start,end]
    
    return _total(0, len(rna))
'''simple kbest'''
#print(total("ACAGU"))
def kbest_simple(rna,K):
#    branch = {(0,0):[]}
    
 #   matrix[0] = {('',''):(0,[])}
    opt = defaultdict(list)
 #   print(rna[1:3])
 

    def _kbest(start,end):
 #       print(start,end)
#        print(rna[start,end])
        matrixes = {}
        one = {}
        h = []
        used = set()
        if rna[start:end] in opt:
            return opt[rna[start:end]]
        if len(rna[start:end]) == 1:
            opt[rna[start:end]] = [(0, '.')]
        elif len(rna[start:end]) == 0:
            opt[rna[start:end]] = [(0, '')]
        if rna[start:end] in opt:
           return opt[rna[start:end]]
        
        for k in range(start + 1, end):
            if rna[start] + rna[k] in pairs:               
                 left = _kbest(start + 1,k)
                 right = _kbest(k + 1,end)
                 matrixes[rna[start + 1:k], rna[k + 1:end]] = []
                 heapq.heappush(h,(-(left[0][0] + right[0][0] + 1), ( rna[start + 1:k], rna[k + 1:end] ),'(' + left[0][1] + ')' + right[0][1] ,0 ,0))
                 used.add((( rna[start + 1:k], rna[k + 1:end] ) , 0, 0))
                 for i,l in enumerate(left):
                     matrixes[rna[start + 1:k], rna[k + 1:end]].append([])
                     for j,r in enumerate(right):
 #                        print(matrixes[rna[start + 1:k], rna[k + 1:end]])
#                         print(matrixes[rna[start + 1:k], rna[k + 1:end]][i])
                         matrixes[rna[start + 1:k], rna[k + 1:end]][i].append((l[0] + r[0] + 1, '(' + l[1] + ')' + r[1]))
                         opt[rna[start:end]].append((l[0] + r[0] + 1, '(' + l[1] + ')' + r[1]))
        one = []
        np = _kbest(start + 1,end)
 #       print(start + 1,end)
#        print(np)
 #       print(np[0])
 #       print( np[0][1])
        heapq.heappush(h,(-(np[0][0]), ('1','1'), '.' + np[0][1],0 ,0))
        used.add((('1','1'),0,0))
        for s in np:
#            print(s)
 #           print(s[0])
#            print(s[1])
            one.append((s[0], '.' + s[1]))
            opt[rna[start:end]].append((s[0], '.' + s[1]))
        '''
        if(len(opt[rna[start:end]]) > K):
            
            res = sorted(opt[rna[start:end]])
            res = reversed(res)
            return list(res)[0:K]
        '''
 #       print(matrixes)
#        print(one)
 #       n = len(matrixes)
 #       print(h)
 #       if len(opt[rna[start:end]]) > K:
        res = []
        def put(k, i, j):
            if k != ('1', '1'):
                if (k, i, j) not in used and i < len(matrixes[k])  and j < len(matrixes[k][i]):
                    
                    heapq.heappush(h, (-(matrixes[k][i][j][0]), k, matrixes[k][i][j][1],i, j))
                    used.add((k , i, j))
            else:
                if j == 0:
                    
                    if (k, i, j) not in used and i < len(one):
#                           print(k,i,j)
#                            print((one[i][0]), k, one[i][1],i, j)
                        heapq.heappush(h, (-(one[i][0]), k, one[i][1],i, j))

        while len(res) < K and h != []:
            
            v, k, s, i, j = heapq.heappop(h)
#               print(v, k, s, i, j)
            res.append((-v, s))
#               print("**")
#                print(res)
            put(k, i + 1, j)
            put(k, i, j + 1)
#           print(res)
        opt[rna[start:end]] = res
 #       print(start,end)
#        print(opt[rna[start:end]])
        return opt[rna[start:end]]
    
    return _kbest(0,len(rna))
'''good kbest'''
def kbest_good(rna,K):
#    branch = {(0,0):[]}
    
 #   matrix[0] = {('',''):(0,[])}
    opt = defaultdict(list)
 #   print(rna[1:3])
 

    def _kbest(start,end):
        if rna[start:end] in opt:
           return opt[rna[start:end]]
        if len(rna[start:end]) == 1:
            opt[rna[start:end]] = [(0, '.')]
            return opt[rna[start:end]]
        elif len(rna[start:end]) == 0:
            opt[rna[start:end]] = [(0, '')]
            return opt[rna[start:end]]
        matrix = []
        one = {}
        h = []
        used = set()

        
        matrixn = 0
        for k in range(start + 1, end):
            if rna[start] + rna[k] in pairs:               
                 left = _kbest(start + 1,k)
                 right = _kbest(k + 1,end)
                 matrix.append(((start + 1, k),(k + 1, end)))
                 heapq.heappush(h,(-(left[0][0] + right[0][0] + 1), matrixn,'(' + left[0][1] + ')' + right[0][1] ,0 ,0))
                 used.add(((start + 1, k),(k + 1, end) , 0, 0))
                 matrixn += 1
                 
        np = _kbest(start + 1,end)
        heapq.heappush(h,(-(np[0][0]), matrixn, '.' + np[0][1],0 ,0))
        used.add(((start + 1, end),0))
        matrix.append((start + 1, end))
        #print(len(matrix), matrixn)
        res = []
        def put(k, i, j):
            if k == matrixn:
#                print(j)
#                np = _kbest(matrix[matrixn][0],matrix[matrixn][1])
                if i < len(np) and (matrix[matrixn], i,j) not in used:
                    heapq.heappush(h, (-np[i][0], matrixn, '.' + np[i][1], i, 0))
                    used.add((matrix[matrixn], i, j))

            else:
                left = _kbest(matrix[k][0][0],matrix[k][0][1])
                right = _kbest(matrix[k][1][0],matrix[k][1][1])
                if (matrix[k][0], matrix[k][1], i, j) not in used and i < len(left)  and j < len(right):
                    heapq.heappush(h, (-(left[i][0] + 1 + right[j][0]), k, '('+left[i][1]+')'+right[j][1],i, j))
                    used.add((matrix[k][0], matrix[k][1], i, j))

        while len(res) < K and h != []:
            v, k, s, i, j = heapq.heappop(h)
            res.append((-v, s))
            if k == matrixn:
                put(k, i + 1, j)
            else:
                put(k, i + 1, j)
                put(k, i, j + 1)
#           print(res)
        opt[rna[start:end]] = res
 #       print(start,end)
#        print(opt[rna[start:end]])
        return opt[rna[start:end]]
    
    return _kbest(0,len(rna))

'''best kbest'''
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
        biggers = [x for x in a[1:] if x > pivot]
        k = len(biggers) + 1
        if i == k:
            return a[0]
        elif i < k:
            return qselect(i, biggers)
        elif i > k:
            smallers = [x for x in a[1:] if x <= pivot]
            return qselect(i - k, smallers)           
    if len(qselectarr) > K:
 #       print(len(qselectarr))
        kth = qselect(K, qselectarr)
        newMatrix = []
        newlength = 0
        last = None
#        nl = 0
        for n, m in enumerate(matrix):
            if n != matrixn and m[0][0][0] + m[1][0][0] + 1 > kth:
                newMatrix.append((m[0],m[1]))
                heapq.heappush(h,(-(m[0][0][0] + m[1][0][0] + 1), newlength,'(%s)' % m[0][0][1] + m[1][0][1] ,0 ,0))
 #               nl = newlength
 #               used.add((newlength , 0, 0))
                newlength += 1
            if n == matrixn and m[0][0] > kth:
                last = m[0]
 #               newMatrix.append((m[0]))
                heapq.heappush(h,(-(m[0][0]), newlength, '.%s' %  m[0][1],0 ,0))
 #               used.add((newlength,0,0))
 #               newlength += 1
        if (last is not None and newlength + 1 < K) or (last is None and newlength < K):
            for n, m in enumerate(matrix):
                if n != matrixn and m[0][0][0] + m[1][0][0] + 1 == kth:
                    newMatrix.append((m[0],m[1]))
                    heapq.heappush(h,(-(m[0][0][0] + m[1][0][0] + 1), newlength,'(%s)' % m[0][0][1] + m[1][0][1] ,0 ,0))
                    used.add((newlength , 0, 0))
                    newlength += 1
                if n == matrixn and m[0][0] == kth:
                    last = m[0]
 #                   newMatrix.append((m[0]))
                    heapq.heappush(h,(-(m[0][0]), newlength, '.%s' %  m[0][1],0 ,0))
    #                used.add((newlength,0,0))
  #                  newlength += 1
                if (last is not None and newlength + 1== K) or (last is None and newlength == K):
                    break
        if last is not None:
            newMatrix.append((last))
            used.add((len(matrix) - 1,0,0))
        matrix = newMatrix
        matrixn = len(matrix) - 1
        '''
        print(qselectarr, kth)
        for n1,m1 in enumerate(newMatrix):
            print(n1,m1)
        print()
        print()
        '''
        
        
        
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
 #       if k > K:
#            print(k,K)
        res.append((-v, s))
        if k == matrixn:
            i += 1
            if i < len(np) and (k, i,j) not in used:
                heapq.heappush(h, (-np[i][0], k, '.%s' % np[i][1], i, 0))
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

rna_element = ['A', 'C', 'G', 'U']
def random_rna(length): return ''.join([random.choice(rna_element) for _ in range(length)])
print(kbest(random_rna(200), 9))

