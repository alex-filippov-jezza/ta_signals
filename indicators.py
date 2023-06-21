import pandas as pd
import talib
import numpy as np
from talib import MA_Type


def macd_build(data, fast_period, slow_period, signal_period):
    # Рассчитываем MACD индикатор
    macd, signal, _ = talib.MACD(data['Close'], fastperiod=fast_period, slowperiod=slow_period,
                                 signalperiod=signal_period)

    return macd, signal


def ma_build(data, ma_period):
    ma = talib.EMA(data['Close'], timeperiod=ma_period)

    return ma


def bollinger_bands(data):
    period = 20

    upper, middle, lower = talib.BBANDS(data['Close'], timeperiod=period, nbdevup=2, nbdevdn=2, matype=MA_Type.EMA)

    return upper, middle, lower
