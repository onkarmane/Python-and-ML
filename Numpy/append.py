import numpy as np
# # To append (along axis=0) r rows to mxn make sure you have r rows and n columns
# # To append(along axix =1) c cols to mxn make sure you have c cols  and m rows

arr = np.ones((3, 3), dtype=int)
print(arr.shape)
arr = np.append(arr, [[9, 9, 9], [1, 1, 1], [3, 3, 3]], axis=1)
print(arr)
