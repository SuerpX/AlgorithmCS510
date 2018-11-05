from collections import defaultdict
def lis(s):
    length = len(s)
    opt = defaultdict(int)
    forward = defaultdict(int)
    def _lis(n):
        if n in opt:
            return opt[n]
        maxI = -1
        isBigger = False
        for x in range(n + 1, length):
 #          print(s[x],s[n])
            if s[x] > s[n]:
                isBigger = True
                num = _lis(x) + 1
                if num > opt[n]:
                    opt[n] = num
                    maxI = x
        if maxI != -1:
            forward[n] = maxI
        if not isBigger:
            opt[n] = 1
            forward[n] = -1
        return opt[n]
    longest = 0
    longestNum = 0
    for i in range(length):
        if i not in opt:
 #           print(opt)
            l = _lis(i)
        l = opt[i]
        if l > longest:
            longest = l
            longestNum = i
            
    def traceForward(w):
 #       print(w)
        if forward[w] == -1:
            return s[w]
        return traceForward(forward[w]) + s[w]
    res = traceForward(longestNum)
    res = res[::-1]
    return longest, res
print(lis("aebbcg"))
print(lis("bdbabebtbsdbcxjhzxncbuqhwirheoiusakjsmnxncbvzbjdshjfnkendcviuheoiowpjotnsnvcxmnzfhjxkhvjsahdhjwgnuhgivdsf"))
        
print(lis("aebbcg"))
print(lis("zyx"))
print(lis("1234567890"))
print(lis("x"))
