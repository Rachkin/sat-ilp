import pycosat
from itertools import combinations, product

n = 10

edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 0],
    [0, 5],
    [1, 6],
    [2, 7],
    [3, 8],
    [4, 9],
    [5, 7],
    [6, 8],
    [7, 9],
    [8, 5],
    [9, 6]
]



def w(v, c):
    return n*v + c + 1


for k in range(1, n+1):
    clause = []
    for v in range(n):
        t = []
        for c in range(k):
            t.append(w(v, c))
        clause.append(t)
        for (c1, c2) in combinations(range(k), 2):
            clause.append([-w(v, c1), -w(v, c2)])

    for e in edges:
        for c in range(k):
            clause.append([-w(e[0], c), -w(e[1], c)])

    ans = pycosat.solve(clause)

    if type(ans) != type(' '):
        print(k)
        for v in range(n):
            for c in range(k):
                if ans[w(v, c) - 1] > 0:
                    print(str(v) + ' ' + str(c))
        exit(0)

