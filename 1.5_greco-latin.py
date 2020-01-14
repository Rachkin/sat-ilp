import pycosat
from itertools import combinations, product


n = 7

clause = []

def v(i, j, c, p):
    return n**3 * c + n**2 * p + n * i + j + 1

def w(i, j, c1, c2):
    return n**4 + n**3 * c1 + n * n * c2 + n * i + j + 1

def vv(i, j, c, p):
    return v(i, j, c, p) - 1

for (i, j) in product(range(n), range(n)):
    for (c1, c2) in combinations(range(n), 2):
        clause.append([-v(i, j, c1, 1), -v(i, j, c2, 1)])
        clause.append([-v(i, j, c1, 2), -v(i, j, c2, 2)])
    t1 = []
    t2 = []
    for c in range(n):
        t1.append(v(i, j, c, 1))
        t2.append(v(i, j, c, 2))
    clause.append(t1)
    clause.append(t2)

for i in range(n):
    for c in range(n):
        t1 = []
        t2 = []
        for j in range(n):
            t1.append(v(i, j, c, 1))
            t2.append(v(i, j, c, 2))
        clause.append(t1)
        clause.append(t2)
        t1 = []
        t2 = []
        for j in range(n):
            t1.append(v(j, i, c, 1))
            t2.append(v(j, i, c, 2))
        clause.append(t1)
        clause.append(t2)
        for (j1, j2) in combinations(range(n), 2):
            clause.append([-v(i, j1, c, 1), -v(i, j2, c, 1)])
            clause.append([-v(i, j1, c, 2), -v(i, j2, c, 2)])
            clause.append([-v(j1, i, c, 1), -v(j2, i, c, 1)])
            clause.append([-v(j1, i, c, 2), -v(j2, i, c, 2)])



for (i1, i2) in product(range(n), range(n)):
    for (j1, j2) in product(range(n), range(n)):
        for (c1, c2) in product(range(n), range(n)):
            if i1 == i2 and j1 == j2:
                continue
            clause.append([-v(i1, j1, c1, 1), -v(i1, j1, c2, 2), -v(i2, j2, c1, 1), -v(i2, j2, c2, 2)])

ans = pycosat.solve(clause)



if(type(ans) == type(' ')):
    print(ans)
else:
    for i in range(n):
        s = ''
        for j in range(n):
            for c in range(n):
                if ans[vv(i, j, c, 1)] > 0:
                    s += str(c+1)
            for c in range(n):
                if ans[vv(i, j, c, 2)] > 0:
                    s += str(c+1)
            if j != n-1:
                s += '-'
        print(s)