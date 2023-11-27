import pandas as pd
import random

# Решение за O(nm)
def one_hot_encoding(df):
    for colname in df['whoAmI'].unique():
        df[colname] = df['whoAmI'].apply(lambda x: 1 if x == colname else 0)
    return df.drop(['whoAmI'], axis=1)

# Решение за O(m + n)
def one_hot_encoding1(df):
    for colname in df['whoAmI'].unique():
        df[colname] = [0] * len(df)
    for row in range(len(df)):
        df.loc[row, df.loc[row, 'whoAmI']] = 1
    return df.drop('whoAmI', axis=1)

# Генерация данных
random.seed(42)
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Применение функций
data1 = one_hot_encoding(data.copy())
data2 = one_hot_encoding1(data.copy())

# Вывод результатов
print("Original DataFrame:")
print(data)
print("\nResult using one_hot_encoding:")
print(data1)
print("\nResult using one_hot_encoding1:")
print(data2)
