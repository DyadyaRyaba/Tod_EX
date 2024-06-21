import numpy as np

# Создаем последовательность чисел от 1 до 109
numbers = np.arange(1, 110)

# Функция для выбора нужных элементов
def select_elements(arr):
    selected = []
    for i in range(0, len(arr), 10):
        row = arr[i:i+10]
        selected.extend([row[0], row[1], row[3], row[6], row[7], row[8]])
    return np.array(selected)

# Выбираем нужные элементы и преобразуем в матрицу 11 на 6
selected_numbers = select_elements(numbers)
matrix = selected_numbers.reshape(11, 6)

# Выводим результат
print(matrix)
