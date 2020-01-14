import pycosat
from itertools import combinations, product


n = 12
m = 10

clause = []

def v(i, j):
    return m * i + j + 1

def vv(i, j):
    return v(i, j) - 1

for (i, j) in product(range(n), range(m)):
    if j <= m - 4:
        clause.append([-v(i, j1) for j1 in range(j, j+4)])
        clause.append([v(i, j1) for j1 in range(j, j + 4)])
    if i <= n - 4:
        clause.append([-v(i1, j) for i1 in range(i, i + 4)])
        clause.append([v(i1, j) for i1 in range(i, i + 4)])
    if i <= n - 4 and j <= m - 4:
        clause.append([-v(i + d, j + d) for d in range(4)])
        clause.append([v(i + d, j + d) for d in range(4)])
    if i >= 3 and j <= m - 4:
        clause.append([-v(i - d, j + d) for d in range(4)])
        clause.append([v(i - d, j + d) for d in range(4)])

task = '''
X....X.XX.
.X.XX...0.
0.X0.X..0X
..........
.X........
.0X...00.X
0..X....X.
0..0..X...
........X.
00....0.X.
.00......X
000.0.X.XX
'''
#print(len(task))

for (i, j) in product(range(n), range(m)):
    if task[vv(i, j) + i + 1] == 'X':
        clause.append([v(i, j)])
    if task[vv(i, j) + i + 1] == '0':
        clause.append([-v(i, j)])




ans = pycosat.solve(clause)

if(type(ans) == type(' ')):
    print(ans)
else:
    for i in range(n):
        s = ''
        for j in range(m):
            if ans[vv(i, j)] > 0:
                s += 'X'
            else:
                s += '0'
        print(s)