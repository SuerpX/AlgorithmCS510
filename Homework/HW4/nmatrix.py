import heapq
from random import randint
def nmatrix(N):
    n = len(N)
    h = []
    used = set()
    res = []
    def put(k, i, j):
        if (k, i, j) not in used and i < n and j < n:
            heapq.heappush(h, (N[k][i][j], k , i, j))
            used.add((k , i, j))
    for i in range(n):
        put(i, 0, 0)
    while len(res) < n:
        v, k, i, j = heapq.heappop(h)
        res.append(v)
        put(k, i + 1, j)
        put(k, i, j + 1)
    return res

def createRandomMatrix(n):
    m = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    m[x][i][j] = randint(1, 10)
                    continue
                if j == 0:
                    m[x][i][j] = m[x][i-1][j] + randint(1, 10)
                    continue
                if i == 0:
                    m[x][i][j] = m[x][i][j-1] + randint(1, 10)
                    continue
                m[x][i][j] = max(m[x][i-1][j], m[x][i][j-1]) + randint(1, 10)
    return m
'''
testcase3 = [[[1,2,4,5,6], [2,3,5,6,7], [4,5,6,7,8], [5,6,7,8,9],[6,7,8,9,10]],
                 [[11, 12, 13, 14, 15], [12, 13, 14, 15, 16], [13, 14, 15, 16, 17], [14, 15, 16, 17, 18], [15, 16, 17, 18, 19]],
                 [[11, 12, 13, 14, 15], [12, 13, 14, 15, 16], [13, 14, 15, 16, 17], [14, 15, 16, 17, 18], [15, 16, 17, 18, 19]],
                 [[11, 12, 13, 14, 15], [12, 13, 14, 15, 16], [13, 14, 15, 16, 17], [14, 15, 16, 17, 18], [15, 16, 17, 18, 19]],
                 [[11, 12, 13, 14, 15], [12, 13, 14, 15, 16], [13, 14, 15, 16, 17], [14, 15, 16, 17, 18], [15, 16, 17, 18, 19]]]

print(nmatrix(testcase3))
'''

testcase4 = createRandomMatrix(100)
print(nmatrix(testcase4))
