from random import randint
from sys import stdin

'''
使用Freivalds比较算法，即测试A(Bx)=Cx是否相等
'''
'''
第一行输入一个整数，接下来输入3n行
'''


def readarray(typ):
    return list(map(typ, stdin.readline().split()))


def readmatrix(n):
    M = []
    for _ in range(n):
        row = readarray(int)
        assert len(row) == n
        M.append(row)
    return M


def mult(M, v):
    n = len(M)
    return [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]


def freivalds(A, B, C):
    n = len(A)
    x = [randint(0, 1000000) for j in range(n)]
    return mult(A, mult(B, x)) == mult(C, x)


num = int(input())
A = readmatrix(num)
B = readmatrix(num)
C = readmatrix(num)
print(freivalds(A, B, C))
