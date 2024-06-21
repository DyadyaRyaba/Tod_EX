import pandas as pd

# Загрузка данных из файлов (здесь мы используем абстрактные имена файлов)
recipes = pd.read_csv('path_to_recipes_sample.csv')
reviews = pd.read_csv('path_to_reviews_sample.csv', index_col=0)

# Объединение таблиц по идентификатору рецепта
merged_df = pd.merge(recipes, reviews, how='inner', left_on='id', right_on='recipe_id')

# Удаление записей рецептов без отзывов (уже выполнено с помощью how='inner')
# Создание нового DataFrame с необходимыми столбцами
final_df = merged_df[['id', 'name', 'date', 'review']]

# Фильтрация записей не старше 2015 года
filtered_df = final_df[pd.to_datetime(final_df['date']).dt.year >= 2015]

# Создание DataFrame с количеством отзывов на каждый рецепт
reviews_count_df = filtered_df.groupby('id').size().reset_index(name='review_count')

# Вывод результатов для проверки
import ace_tools as tools; tools.display_dataframe_to_user(name="Final DataFrame with Reviews", dataframe=final_df)
import ace_tools as tools; tools.display_dataframe_to_user(name="Filtered Reviews Count DataFrame", dataframe=reviews_count_df)

# Вывод первых строк для проверки
print("Final DataFrame with Reviews:")
print(final_df.head())

print("\nFiltered Reviews Count DataFrame:")
print(reviews_count_df.head())
