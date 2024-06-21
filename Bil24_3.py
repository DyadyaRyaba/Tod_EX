import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из файла
file_path = '/mnt/data/average_ratings.csv'
data = pd.read_csv(file_path, parse_dates=['Date'])

# Построение графика
plt.figure(figsize=(10, 6))
for recipe in data.columns[1:]:
    plt.plot(data['Date'], data[recipe], label=recipe)

plt.xlabel('Date')
plt.ylabel('Average Rating')
plt.title('Average Ratings of Recipes Over Time')
plt.legend()
plt.grid(True)
plt.show()