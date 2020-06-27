import numpy as np
import matplotlib.pyplot as plt
arr = np.random.randint(1, 10, 20)
numbers = [x for x in range(20)]
# plt.plot(numbers, arr)
plt.plot(numbers, arr)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
