import numpy as np

# Создание двумерного массива случайных целых чисел от 0 до 15 размером 10x8
np.random.seed(0)  # Устанавливаем seed для воспроизводимости результатов
ar1 = np.random.randint(0, 16, size=(10, 8))

# Замена нечетных элементов на -1
ar1[ar1 % 2 != 0] = -1

# Вывод результата
print(ar1)