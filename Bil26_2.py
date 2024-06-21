import numpy as np

# Создание двумерных массивов случайных целых чисел от -5 до 5 размером 10x4
np.random.seed(0)  # Устанавливаем seed для воспроизводимости результатов
ar1 = np.random.randint(-5, 6, size=(10, 4))
ar2 = np.random.randint(-5, 6, size=(10, 4))

# Удвоение значений ar1, которые больше значений ar2, и обнуление остальных
result = np.where(ar1 > ar2, ar1 * 2, 0)

# Вывод исходных массивов и результата
print("Array ar1:")
print(ar1)
print("\nArray ar2:")
print(ar2)
print("\nResulting array:")
print(result)
