import numpy as np

# Загрузка данных из файла
file_path = 'path_to_minutes_n_ingredients.csv'  # Замените на реальный путь к файлу

# Загрузка данных с указанием разделителя (запятая) и типа данных
data = np.loadtxt(file_path, delimiter=',', dtype=np.int32)

# Вывод первых 5 строк массива
print(data[:5])
