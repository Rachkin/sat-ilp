from itertools import combinations, product
from mip.model import *

n = 5

model = Model(sense=MAXIMIZE, solver_name="cbc")

segments = {}
for i, j in product(range(n + 1), repeat=2):
    for delta_i, delta_j in product((-1, 1), repeat=2):
        if i + delta_i in range(n + 1) and j + delta_j in range(n + 1):
            segments[i, j, i + delta_i, j + delta_j] = model.add_var(var_type=BINARY)

for s1, s2 in combinations(segments, 2):
    if LineString([s1[:2], s1[2:]]).intersects(LineString([s2[:2], s2[2:]])):
        model += segments[s1] + segments[s2] <= 1

model.objective = xsum(segments.values())
model.optimize()

for s in segments:
    if abs(segments[s].x) > 1e-6:
        print(s)