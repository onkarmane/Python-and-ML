import numpy as np

# Using Vstack : Adding to axis 0 so axis 1 should match 
arr1 = np.ones((1, 3), dtype=int)
arr0 = np.zeros((1, 3))
vs = np.vstack((arr1, arr0))
print(vs.shape)
print(vs)

# #Using hstack : Adding to axis 1 so axis 0 should match.
arr1 = np.ones((2, 3))
arr0 = np.zeros((2, 4))
hs = np.hstack((arr1, arr0))
print(hs.shape)
print(hs)
