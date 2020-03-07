
import random
import time
import math

def stopwatch(f, n, k):
    start = time.perf_counter()
    res = f(n, k)
    end = time.perf_counter()
    return end - start

cnt = 0
tot = 0

def getDigit(n):
    if n == 0:
        return 1
    ret = 0
    while n > 0:
        n //= 2
        ret += 1
    return ret

def binom_BF(n, k):
    global cnt, tot
    if k==0 or k==n:
        return 1
    else:
        ret = binom_BF(n-1, k-1) + binom_BF(n-1, k)
        tot += getDigit(ret)
        cnt += 1
        print(n, k)
        return ret

def binom_DP(n, k):
    f = []
    for i in range(n+1):
        f.append([])
        for j in range(k+1):
            f[i].append(0)
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j==0 or j==i:
                f[i][j] = 1
            else:
                f[i][j] = f[i-1][j-1] + f[i-1][j];
    return f[n][k]

def calForBF():
    for i in range(10, 28):
        for j in range(10, 11):
            if j <= i:
                t = stopwatch(binom_BF, i, j)
                print(t)
            else:
                print(0)

for i in range(14, 15):
    for j in range(7, 8):
        cnt = 0
        tot = 0
        x = binom_BF(i, j)
        if cnt > 0:
            print(i, j, x, cnt, tot)

def getcount():
    for n in range(10, 28):
        for k in range(10, 11):
            res = 0
            for i in range(n+1):
                for j in range(k+1):
                    res += binom_DP(n, i) * binom_DP(k, j)
            print(res)

    print("")

    for n in range(10, 28):
        for k in range(10, 11):
            res = 0
            for i in range(n+1):
                for j in range(k+1):
                    t = binom_DP(n, i) * binom_DP(k, j) 
                    if t > 0:
                        print(i, j, binom_DP(i, j))
                        t = t * math.log2(binom_DP(i, j))
                    res += t
            print(res)

