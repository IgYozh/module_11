import numpy as np

# Создаем массив с помощью класса numpy.ndarray
data = np.ndarray((3, 3), buffer=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), dtype=int)

print("Массив, созданный с помощью класса numpy.ndarray:")
print(data)

import numpy as np

# Создаем одномерный массив
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Используем метод reshape для изменения формы массива
reshaped_data = data.reshape((3, 3))

print("Массив после изменения формы с помощью метода reshape:")
print(reshaped_data)

import numpy as np

# Определяем два матрицы
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Используем функцию numpy.dot для умножения матриц
result = np.dot(matrix_a, matrix_b)

print("Результат умножения двух матриц с помощью функции numpy.dot:")
print(result)
