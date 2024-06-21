import pandas as pd

# Пути к файлам (замените на реальные пути при необходимости)
recipes_file_path = 'path_to_recipes_sample.csv'
reviews_file_path = 'path_to_reviews_sample.csv'

# Загрузка данных из файла recipes_sample.csv
recipes = pd.read_csv(recipes_file_path)

# Загрузка данных из файла reviews_sample.csv с корректной обработкой безымянного столбца (индексы)
reviews = pd.read_csv(reviews_file_path, index_col=0)

# Вывод первых строк для проверки
print("Recipes DataFrame:")
print(recipes.head())

print("\nReviews DataFrame:")
print(reviews.head())
