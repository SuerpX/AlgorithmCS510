__author__ = "Liang Huang"

from collections import defaultdict

def lis(s):
    def solution(i):
        return "" if i<0 else solution(back[i]) + chr(a[i]) # int to char

    a = list(map(ord, s)) + [float("inf")] # convert chars to ints
    d = defaultdict(int)
    back = defaultdict(lambda :- 1)
    for j, cj in enumerate(a):
        for k, ck in enumerate(a[:j]):
            print(chr(cj),chr(ck), d[k])
            if ck < cj and d[k] + 1 > d[j]:
 #               print(d[k])
                d[j] = d[k] + 1
                back[j] = k
    print(d)
    return solution(back[len(a)-1]) # exclude the final padding

if __name__=="__main__":
    print(lis("aebbcg"))
    '''
    print(lis("zyx"))
    print(lis("1234567890"))
    print(lis("x"))
    print(lis(""))
    '''
