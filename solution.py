import pandas as pd
import numpy as np
from scipy.stats import stats

chat_id = 241769496 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
        # Применяем критерий Стьюдента для проверки однородности выборок
    _, pvalue = stats.ttest_ind(x, y)
    return pvalue >= 0.1 # Ваш ответ, True или False
