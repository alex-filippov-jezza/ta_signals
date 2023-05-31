import pandas as pd


def macd_build(data, fast_period, slow_period, signal_period):
    # Рассчитываем MACD индикатор
    exp1 = data['Close'].ewm(span=fast_period, adjust=False).mean()
    exp2 = data['Close'].ewm(span=slow_period, adjust=False).mean()
    macd = exp1 - exp2

    # Рассчитываем сигнальную линию для MACD
    signal = macd.ewm(span=signal_period, adjust=False).mean()

    return macd, signal


def ma_build(data, ma_period):
    ma = data['Close'].rolling(window=ma_period).mean()

    return ma
