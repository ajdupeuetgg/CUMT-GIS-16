# -*- coding:utf-8 -*-

import numpy as np
import math


class Matrix:
    def __init__(self):
        self.Row = 0
        self.Column = 0
        self.M = []

    def blank_in(self):
        M0 = []
        for i in range(1, self.Row + 1):
            x = input("请输入第{}行数据：".format(i))
            x0 = list(map(float, x.rstrip().split()))
            M0.append(x0)
        print("")
        self.M = M0


f = open(r'/Users/apple/Documents/test/con.txt')
lines = f.readlines()
f.close()

w = int(lines[1])
H = list(map(float, lines[3].rstrip().split()))
g = list(map(float, lines[4].rstrip().split()))
j = list(map(float, lines[5].rstrip().split()))

A = Matrix()
A.Row = len(g) - w
A.Column = len(g)
A.blank_in()
AA = np.mat(A.M)

W = Matrix()
W.Row = len(g) - w
W.Column = 1
W.blank_in()
WW = np.mat(W.M)

P = []
for i in range(len(j)):
    P.append([])
    for ii in range(len(j)):
        P[i].append(0)
for i in range(len(j)):
    P[i][i] = j[i]
PP = np.mat(P)

Naa = AA * PP * AA.T
KK = -Naa.I * WW
VV = PP * AA.T * KK

V = VV.tolist()
for i in range(len(g)):
    g[i] += (V[i][0] / 1000)
    print("h{}的改正后的结果为{}".format(i + 1, g[i]))

VTPV = KK.T * Naa * KK
sigma = math.sqrt(VTPV[0, 0] / (len(g) - w))
print("精度评定：")
print("单位权中误差为：{}".format(sigma))
