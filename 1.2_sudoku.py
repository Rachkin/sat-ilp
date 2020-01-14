import pycosat
from itertools import combinations, product

clause = []

n = 9
nn = 3

def v(i, j, k):
    return n*n * i + n * j + k + 1

for i in range(n):
    for j in range(n):
        for (c1, c2) in combinations(range(n), 2):
            clause.append([-v(i, j, c1), -v(i, j, c2)])

for i in range(n):
    for c in range(n):
        for (j1, j2) in combinations(range(n), 2):
            clause.append([-v(i, j1, c), -v(i, j2, c)])
            clause.append([-v(j1, i, c), -v(j2, i, c)])

for ii in range(nn):
    for jj in range(nn):
        for c in range(n):
            for (i1, i2) in combinations(range(nn), 2):
                for (j1, j2) in combinations(range(nn), 2):
                    clause.append([-v(ii * nn + i1, jj * nn + j1, c), -v(ii * nn + i2, jj * nn + j2, c)])

for i in range(n):
    for j in range(n):
        t = []
        for c in range(n):
            t.append(v(i, j, c))
        clause.append(t)
need = []
string = """
* 	1 	* 	5 	*	*	3   *   *  
*	*	2 	8   *   *   *   *   *    
*	*	3 	*	*	*	1 	9   * 
*	2 	*	*	*	9 	*	1   *
6 	4 	*	*	*	*	*	5   * 
5 	*	*	*	*	1 	*	2   *
*	*	*	*	7 	*	*	*	6
*	*	*	*	6 	2 	*	*	7
*	9   *   *   *   *   *   *   *"""

vr = 0
#'''
for c in string:
    if ord('0') <= ord(c) and ord(c) <= ord('9'):
        print(str(vr // 9) + ' ' + str(vr % 9) + ' ' + str(int(c)-1))
        clause.append([vr*n + int(c)])
        vr += 1
    if c == '*':
        vr += 1
#'''


ans = pycosat.solve(clause)

if type(ans) == type('dfdf'):
    print(ans)
else:
    for i in range(n):
        s = ''
        for j in range(n):
            for c in range(n):
                if ans[v(i, j, c) - 1] > 0:
                    s = s + str(c+1);
                    break
            s += ' '
        print(s)



