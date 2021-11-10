import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kstest, norm

U1 = np.random.uniform(-1,1,size = 100)

ks_statistic, p_value = kstest(U1, 'norm')
print(ks_statistic, p_value)