import pandas as pd

# Загрузка данных из файла sp500hst.txt
sp500hst_path = '/mnt/data/sp500hst.txt'
sp500_data = pd.read_csv(sp500hst_path, header=None, names=["date", "ticker", "open", "high", "low", "close", "volume"])

# Загрузка данных из файла sp_data2.csv
sp_data2_path = '/mnt/data/sp_data2.csv'
ticker_data = pd.read_csv(sp_data2_path)

# Объединение данных по тикеру
merged_data = pd.merge(sp500_data, ticker_data, how='left', left_on='ticker', right_on='Ticker Symbol')

# Обработка случаев с отсутствием данных об именах тикеров
merged_data['Company Name'].fillna('Unknown', inplace=True)

# Удаление столбца 'Ticker Symbol' из ticker_data, если он дублируется
merged_data.drop(columns=['Ticker Symbol'], inplace=True)

import ace_tools as tools; tools.display_dataframe_to_user(name="Merged SP500 Data", dataframe=merged_data)

# Вывод первых строк объединенных данных
print(merged_data.head())
