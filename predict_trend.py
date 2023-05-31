import pandas as pd
from indicators import macd_build
from optimal_parameters import find_optimal_macd_parameters


def predict_trend_ma(data, ma_period):
    # Рассчитываем скользящее среднее
    ma = data['Close'].rolling(window=ma_period).mean()

    # Определяем направление тренда на основе расположения цены относительно скользящей средней
    if data['Close'].iloc[-1] > ma.iloc[-1]:
        trend_direction = 'Uptrend'
    elif data['Close'].iloc[-1] < ma.iloc[-1]:
        trend_direction = 'Downtrend'
    else:
        trend_direction = 'Sideways'

    return trend_direction


def predict_trend_macd(data):
    fast, slow, signal = find_optimal_macd_parameters(data)

    # Рассчитываем MACD индикатор
    macd, signal = macd_build(data, fast, slow, signal)



    # Определяем направление тренда на основе расположения MACD линии и сигнальной линии
    if macd.iloc[-1] > signal.iloc[-1]:
        trend_direction = 'Uptrend'
    elif macd.iloc[-1] < signal.iloc[-1]:
        trend_direction = 'Downtrend'
    else:
        trend_direction = 'Sideways'

    return trend_direction


def predict_trend(data, ma_period):
    ma_trend = predict_trend_ma(data, ma_period)
    macd_trend = predict_trend_macd(data)

    if ma_trend == macd_trend:
        trend_direction = ma_trend
    else:
        trend_direction = 'Sideways'

    return trend_direction


