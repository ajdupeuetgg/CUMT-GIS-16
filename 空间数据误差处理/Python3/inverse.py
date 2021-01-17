# -*- coding:utf-8 -*-

class Matrix:
    def __init__(self):
        self.Row = int(input("请输入方阵阶数："))
        self.M = self.blank_in()

    def blank_in(self):
        M0 = []
        for i in range(1, self.Row + 1):
            x = input("请输入第{}行数据：".format(i))
            x0 = list(map(float, x.rstrip().split()))
            M0.append(x0)
        return M0

    def Inverse(self):
        def Identity(m):
            n = len(m)
            l = []
            for i in range(n):
                l.append([])
                for j in range(n):
                    if i == j:
                        l[i].append(1)
                    else:
                        l[i].append(0)
            return l

        def Swap(m):
            n = len(m)
            swap = []
            l = []
            for i in range(n):
                swap.append(i)
                l.append([])
                for j in range(n):
                    l[i].append(0)

            for i in range(n):
                max_row = m[i][i]
                row = i
                for j in range(i, n):
                    if m[j][i] >= max_row:
                        max_row = m[j][i]
                        row = j
                swap[i] = row

                if row != i:
                    for j in range(n):
                        m[i][j], m[row][j] = m[row][j], m[i][j]

                for j in range(i + 1, n):
                    if m[j][i] != 0:
                        l[j][i] = m[j][i] / m[i][i]
                        for k in range(0, n):
                            m[j][k] = m[j][k] - (l[j][i] * m[i][k])

            return swap, m, l

        def Step(m):
            n = len(m)
            long = len(m) - 1
            l = []
            for i in range(n):
                l.append([])
                for j in range(n):
                    l[i].append(0)

            for i in range(n-1):
                for j in range(long-i):
                    if m[long-i-j-1][long-i] != 0 and m[long-i][long-i] != 0:
                        l[long-i-j-1][long-i] = m[long-i-j-1][long-i] / m[long-i][long-i]
                        for k in range(n):
                            m[long-i-j-1][k] = m[long-i-j-1][k] - l[long-i-j-1][long-i] * m[long-i][k]

            return m, l

        def Diagonal(m):
            n = len(m)
            l = []
            for i in range(n):
                l.append(m[i][i])
            return l

        def Gauss_Jordan(matrix):
            n = len(matrix)
            new = Identity(matrix)
            (swap, matrix1, l1) = Swap(matrix)
            (matrix2, l2) = Step(matrix1)
            l3 = Diagonal(matrix2)
            for i in range(n):
                if swap[i] != i:
                    new[i], new[swap[i]] = new[swap[i]], new[i]
                for j in range(i+1, n):
                    for k in range(n):
                        if l1[j][i] != 0:
                            new[j][k] = new[j][k] - l1[j][i] * new[i][k]
            for i in range(n-1):
                for j in range(n-i-1):
                    if l2[n-1-i-j-1][n-1-i] != 0:
                        for k in range(n):
                            new[n-1-i-j-1][k] = new[n-1-i-j-1][k]-l2[n-1-i-j-1][n-i-1] * new[n-1-i][k]
            try:
                for i in range(n):
                    for j in range(n):
                        new[i][j] = new[i][j] / l3[i]
                return new
            except ZeroDivisionError:
                print("该矩阵不可逆")

        return Gauss_Jordan(t.M)


t = Matrix()
print(t.Inverse())
