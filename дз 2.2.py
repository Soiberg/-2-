import numpy as np
exper = 1000
results = []

for _ in range(exper):
    arr = np.random.randint(1, 11, size=100)
    percentage_greater_than_7 = np.sum(arr > 7) / len(arr) * 100
    results.append(percentage_greater_than_7)

equal_to_20_percent = np.sum(np.array(results) == 20)

print(f"{equal_to_20_percent / experiments * 100}")
