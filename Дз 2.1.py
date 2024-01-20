import numpy as np
arr = np.random.randint(1, 11, size=100)
percentage_greater_than_7 = np.sum(arr > 7) / len(arr) * 100
print(f"{percentage_greater_than_7}%")
