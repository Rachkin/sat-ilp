import pycosat
import time

lst = time.time()

clause = []

n = 4 # 58 fo 1 sec

for i in range(n):
    t = []
    for j in range(n):
        for x in range(n):
            if x != i:
                clause.append([-i*n - j - 1, -x*n - j - 1])
            if x != j:
                clause.append([-i*n - j - 1, -i*n - x - 1])
            if x != i and i + j - x >= 0 and i + j - x < n:
                clause.append([-i*n - j - 1, -x*n - (i + j - x) - 1])
            if x != i and x - (i - j) >= 0 and x - (i - j) < n:
                clause.append([-i*n - j - 1, -x*n - (x - (i - j)) - 1])
        t.append(i*n + j + 1)
    clause.append(t)


#print(clause)
print(time.time() - lst)
ans = pycosat.solve(clause)
#print(pycosat.solve(clause))
for i in range(n):
    s = ''
    for j in range(n):
        if ans[i*n + j] > 0:
            s += 'Q'
        else:
            s += '.'
    print(s)