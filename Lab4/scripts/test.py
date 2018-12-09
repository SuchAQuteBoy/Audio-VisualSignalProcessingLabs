import numpy as np

mat = np.mat([0.098, 0.564, 0.257, 0, 0.439, -0.291, -0.148, 0, -0.071, -0.368, 0.439, 0, 0, 0, 0, 1])

print(mat)
mat[0][0] = 0
print(mat)