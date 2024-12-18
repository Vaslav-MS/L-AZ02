import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Создание DataFrame с данными
np.random.seed(45)  # Для воспроизводимости данных
data = {
    'Имя': ['Алексей', 'Мария', 'Иван', 'Ольга', 'Дмитрий', 'Екатерина', 'Сергей', 'Анна', 'Николай', 'Елена'],
    'Математика': np.random.randint(1, 5, size=10),
    'Физика': np.random.randint(1, 5, size=10),
    'Химия': np.random.randint(1, 5, size=10),
    'Литература': np.random.randint(1, 5, size=10),
    'История': np.random.randint(1, 5, size=10)
}

df = pd.DataFrame(data)

# 2. Вывод первых строк DataFrame
print("Первые несколько строк DataFrame:")
print(df.head())

# 3. Средняя оценка по каждому предмету
mean_ball = df.iloc[:, 1:].mean()
print("\nСредняя оценка по каждому предмету:")
print(mean_ball)

# 4. Медианная оценка по каждому предмету
median_ball = df.iloc[:, 1:].median()
print("\nМедианная оценка по каждому предмету:")
print(median_ball)

# 5. Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print(f"\nQ1 для математики: {Q1_math}")
print(f"Q3 для математики: {Q3_math}")
print(f"IQR для математики: {IQR_math}")

# 6. Стандартное отклонение
std_dev = df.iloc[:, 1:].std()
print("\nСтандартное отклонение оценок по каждому предмету:")
print(std_dev)

