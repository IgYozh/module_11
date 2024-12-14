import pandas as pd

# Создание DataFrame с помощью класса
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Вывод DataFrame
print(df)



# Создание DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}

df = pd.DataFrame(data)

# Использование метода для вычисления среднего значения столбца 'Age'
average_age = df['Age'].mean()

print(f'Средний возраст: {average_age}')



# Чтение данных из CSV-файла с использованием функции read_csv
# Пример содержимого файла:


df = pd.read_csv('data.csv')

# Вывод данных из CSV
print(df)

