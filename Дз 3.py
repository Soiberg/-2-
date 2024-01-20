import pandas as pd
import numpy as np

data = {
    'Column1': np.random.rand(10),
    'Column2': np.random.randint(1, 11, size=10),
    'Column3': np.random.choice(['A', 'B', 'C'], size=10)
}

df = pd.DataFrame(data)
print("Первые 3 строки:")
print(df.head(3))
print("\nПоследние 3 строки:")
print(df.tail(3))
df.to_csv('my_dataframe.csv', index=False)
