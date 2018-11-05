import heapq
from random import *
from time import time

def nsmallest(m):
    H = []
    n = len(m)
    for x in range(n):
        H.append((m[x][0][0], x, 0, 0))
    heapq.heapify(H)
    for _ in range(n-1):
        v, x, i, j = heapq.heappop(H)
        if i+1 < n:
            if (m[x][i+1][j], x, i+1, j) not in H: heapq.heappush(H, (m[x][i+1][j], x, i+1, j))
        if j+1 < n:
            if (m[x][i][j+1], x, i, j+1) not in H: heapq.heappush(H, (m[x][i][j+1], x, i, j+1))
    return heapq.heappop(H)[0]


def qselect(k, a):
    if k < 1 or k > len(a) or a == []:
        return []
    else:
        r_index = randint(0, len(a)-1)
        a[0], a[r_index] = a[r_index], a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        l_left = len(left)
        if k-1 < l_left:
            return qselect(k, left)
        elif k-1 == l_left:
            return pivot
        else:
            right = [x for x in a[1:] if x >= pivot]
            return qselect(k-l_left-1, right)

def naiveNsmallest(m):
    A = []
    n = len(m)
    for x in range(n):
        for i in range(n):
            for j in range(n):
                A.append(m[x][i][j])
    return qselect(n, A)


def print3DMatrix(m):
    print("[")
    for m2 in m:
        for a in m2:
            print(a)
        print("---")
    print("]")
    print("------")

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


if __name__ == '__main__':
    testcase1 = [[[1,2], [3,4]], [[2,3], [4,5]]]
    testcase2 = [[[1,4,5], [4,5,6], [5,6,7]], [[1,3,4], [3,4,5], [4,5,6]], [[1,2,3], [2,3,4], [3,4,5]]]
    testcase3 = [[[1,2,4,5,6], [2,3,5,6,7], [4,5,6,7,8], [5,6,7,8,9],[6,7,8,9,10]],
                 [[11, 12, 13, 14, 15], [12, 13, 14, 15, 16], [13, 14, 15, 16, 17], [14, 15, 16, 17, 18], [15, 16, 17, 18, 19]],
                 [[11, 12, 13, 14, 15], [12, 13, 14, 15, 16], [13, 14, 15, 16, 17], [14, 15, 16, 17, 18], [15, 16, 17, 18, 19]],
                 [[11, 12, 13, 14, 15], [12, 13, 14, 15, 16], [13, 14, 15, 16, 17], [14, 15, 16, 17, 18], [15, 16, 17, 18, 19]],
                 [[11, 12, 13, 14, 15], [12, 13, 14, 15, 16], [13, 14, 15, 16, 17], [14, 15, 16, 17, 18], [15, 16, 17, 18, 19]]]
    #print3DMatrix(testcase1)
    # print3DMatrix(testcase2)
    # print3DMatrix(testcase3)

    testcase4 = createRandomMatrix(100)

    #print3DMatrix(testcase4)

    print("smart: ", nsmallest(testcase1))
    print("naive: ", naiveNsmallest(testcase1))
    print("smart: ", nsmallest(testcase2))
    print("naive: ", naiveNsmallest(testcase2))
    print("smart: ", nsmallest(testcase3))
    print("naive: ", naiveNsmallest(testcase3))
    # print("smart: ", nsmallest(testcase4))
    # print("naive: ", naiveNsmallest(testcase4))

    t= time()
    nsmallest(testcase4)
    print("heap + baby Dijkstra : ", time() -t)
    t= time()
    naiveNsmallest(testcase4)
    print("naive way : ", time() -t)
