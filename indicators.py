import pandas as pd
import talib


def macd_build(data, fast_period, slow_period, signal_period):
    # Рассчитываем MACD индикатор
    macd, signal, _ = talib.MACD(data['Close'], fastperiod=fast_period, slowperiod=slow_period,
                                 signalperiod=signal_period)

    return macd, signal


def ma_build(data, ma_period):
    ma = talib.EMA(data['Close'], timeperiod=20)

    return ma
