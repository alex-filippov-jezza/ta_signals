import pandas as pd
from predict_trend import predict_trend, predict_price
from indicators import macd_build, bollinger_bands
from optimal_parameters import find_optimal_macd_parameters, find_optimal_ema_parameters

# Создаем список данных о ценах
data = pd.read_csv('data.csv', sep=';')

# Рассчитываем MACD индикатор

# Преобразуем список в DataFrame
df = pd.DataFrame(data)

# Вызываем функцию для прогнозирования направления тренда
trend_direction = predict_trend(df)
fast, slow, signal = find_optimal_macd_parameters(df)
ema_period = find_optimal_ema_parameters(df)

# Выводим результат
print('Trend direction:', trend_direction)
print(f"Лучшие параметры MACD: Fast={fast}, Slow={slow}, Signal={signal}")
print(f"Лучшие параметры EMA: {ema_period}")

upper, middle, lower = bollinger_bands(df)
price_prediction = predict_price(data, trend_direction)

print("Диапазон цен на основе EMA и MACD:", price_prediction)
