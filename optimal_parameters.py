import pandas as pd
import numpy as np
from indicators import macd_build


def find_optimal_macd_parameters(data):

    fast_period_range = (2, 100)
    slow_period_range = (2, 100)
    signal_period_range = (1, 50)
    """
    Функция для автоматического подбора оптимальных параметров для MACD.
    """
    false = 20

    best_fast = None
    best_slow = None
    best_signal = None

    for fast in range(fast_period_range[0], fast_period_range[1] + 1):
        for slow in range(slow_period_range[0], slow_period_range[1] + 1):
            for signal in range(signal_period_range[0], signal_period_range[1] + 1):

                if slow > fast * 2:
                    # Вычисляем MACD со всеми возможными значениями параметров
                    macd, macdsignal = macd_build(data, fast, slow, signal)

                    # Оцениваем качество индикатора на текущих параметрах

                    false_count = false_macd_signals(data, macd, macdsignal)

                    # Обновляем лучшие параметры при нахождении нового лучшего значения
                    if false > false_count:
                        best_fast = fast
                        best_slow = slow
                        best_signal = signal
                        false = false_count

    return best_fast, best_slow, best_signal


def false_macd_signals(data, macd_line, signal_line):

    # определение знаков сигналов
    crosses_above = np.where((macd_line > signal_line) & (macd_line.shift(1) <= signal_line.shift(1)), 1, 0)
    crosses_below = np.where((macd_line < signal_line) & (macd_line.shift(1) >= signal_line.shift(1)), 1, 0)

    # определение ложных сигналов
    false_signals = 0
    for i in range(len(crosses_above)):
        if crosses_above[i] == 1 and data['Close'][i] < signal_line[i]:
            false_signals += 1
        elif crosses_below[i] == 1 and data['Close'][i] > signal_line[i]:
            false_signals += 1

    return false_signals



