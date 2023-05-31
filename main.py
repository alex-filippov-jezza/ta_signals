import pandas as pd
from predict_trend import predict_trend
from indicators import macd_build
from optimal_parameters import find_optimal_macd_parameters

# Создаем список данных о ценах
data = pd.read_csv('data.csv', sep=';')

# Рассчитываем MACD индикатор

# Преобразуем список в DataFrame
df = pd.DataFrame(data)



# Вызываем функцию для прогнозирования направления тренда
trend_direction = predict_trend(df, ma_period=3)
fast, slow, signal = find_optimal_macd_parameters(df)

# Выводим результат
print('Trend direction:', trend_direction)
print(f"Лучшие параметры MACD: Fast={fast}, Slow={slow}, Signal={signal}")
