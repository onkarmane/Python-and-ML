import numpy as np

# Syntax to create an np array is np.array(object).So object could be list,tuple or dict.
# Creating array with dict gives zerodimension array.Hence cannot be accessed by arr[index]
# Can be accessed by array.item()

list_arr = np.array(([1, 2, 3, 4, 5]))
dict_arr = np.array({'One': 1, 'Two': 2})
tuple_arr = np.array((1, 2, 3, 4, 5))
print(list_arr, tuple_arr)
print(dict_arr.item())
print(list_arr.ndim, dict_arr.ndim, tuple_arr.ndim)
