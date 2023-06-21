import pandas as pd
from predict_trend import predict_trend, predict_price
from indicators import macd_build, bollinger_bands, ma_build
from optimal_parameters import find_optimal_macd_parameters, find_optimal_ema_parameters
import mplfinance as mpf

# Создаем список данных о ценах
data = pd.read_csv('SBER_210621_230621.csv', sep=';', index_col=0, parse_dates=['Date'])

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
macd, macdsignal = macd_build(df, fast, slow, signal)
ema = ma_build(df, 100)
print(ema)

plots = [
    mpf.make_addplot(ema, color='#1f77b4', panel=0, secondary_y=False),

    mpf.make_addplot(upper, color='#ff0000', panel=0, secondary_y=False),
    mpf.make_addplot(middle, color='#ff0000', panel=0, secondary_y=False),
    mpf.make_addplot(lower, color='#ff0000', panel=0, secondary_y=False),

    mpf.make_addplot(macd, color='#606060', panel=2, ylabel='MACD', secondary_y=False),
    mpf.make_addplot(macdsignal, color='#1f77b4', panel=2, secondary_y=False)]

mpf.plot(df, type='candle', style='yahoo', volume=True, addplot=plots, panel_ratios=(3, 1, 1), figscale=2)
