import pandas as pd

file_path = 'пуууууть сюдаааааааааа дааааааааа'

df = pd.read_csv(file_path)

filtered_data_1 = df[(df['Возраст'] > 30) & (df['Годовой доход'] < 30000)]

filtered_data_2 = df[(df['Профессия'] == 'юрист') & (df['Опыт работы'] > 5)]

print("Люди с возрастом больше 30 и доходом менее 30000:")
print(filtered_data_1)

print("\nЮристы с опытом работы более 5 лет:")
print(filtered_data_2)
