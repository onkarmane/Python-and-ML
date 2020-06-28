import numpy as np
# Using np.c_ : Adds along axis 1 but converts to 2D.
arr1 = np.array([1, 2, 3])
arr0 = np.array([4, 5, 6])
c = np.c_[arr1, arr0]
print(c.shape)
print(c)
hs = np.hstack((arr1, arr0))
print(hs.shape)
print(hs)

# Using np.r_ : Adds along axis 0
arr1 = np.array([[1, 2, 3]])
arr0 = np.array([[4, 5, 6]])
r = np.r_[arr1, arr0]
print(r.shape)
print(r)
vs = np.vstack((arr1, arr0))
print(vs.shape)
print(vs)
