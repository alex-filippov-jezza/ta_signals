import pandas as pd
from indicators import macd_build, ma_build, bollinger_bands
from optimal_parameters import find_optimal_macd_parameters, find_optimal_ema_parameters


def predict_trend_ma(data):
    # Рассчитываем скользящее среднее

    ma_period = find_optimal_ema_parameters(data)

    ma = ma_build(data, ma_period)

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


def predict_trend(data):
    ma_trend = predict_trend_ma(data)
    macd_trend = predict_trend_macd(data)

    if ma_trend == macd_trend:
        trend_direction = ma_trend
    else:
        trend_direction = 'Sideways'

    return trend_direction


def predict_price(data, trend_direction):
    upper, middle, lower = bollinger_bands(data)
    max_price = upper.iloc[-1]
    min_price = lower.iloc[-1]
    price_range = [max_price, min_price]
    if trend_direction == 'Uptrend':
        return max_price
    elif trend_direction == 'Downtrend':
        return min_price
    else:
        return price_range
