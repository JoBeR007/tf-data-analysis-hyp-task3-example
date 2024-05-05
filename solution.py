import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp

chat_id = 441218136 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    # Perform the one-sample t-test
    t_stat, p_value = ttest_1samp(x, 500)

    # Return True if we reject the null hypothesis (p-value < 0.06), False otherwise
    return p_value < 0.06
