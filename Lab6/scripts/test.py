import numpy as np

distance = []
result = []
for i in range(3, 20, 2):
    center = int(i/2)
    for j in range(i):
        for k in range(j):
            d = (i - center) ^ 2 + (j - center) ^ 2
            distance.append(d)
    result.append(np.var(distance))
    distance.clear()
print(result)