import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ttest_ind


chat_id = 346373029 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    y = np.empty(len(x))
    y.fill(500)
    _, pval, _ = ttest_ind(x, y, alternative = 'larger')
    return pval < 0.1
