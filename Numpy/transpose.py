import numpy as np

# To transpose and see: It actually changes dimensions.
arr = np.array([[5, 6]])
print(arr.shape)
print(arr)
arr = arr.T
print(arr.shape)
print(arr)
