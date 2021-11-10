import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kstest, norm
# np.random.seed(521)
normal = np.random.randn(10000000)
U1 = np.random.uniform(size = 10000000)
U2 = np.random.uniform(size = 10000000)
R = np.sqrt(-2 * np.log(U1))
Theta = 2 * np.pi * U2
X = R * np.cos(Theta)
Y = R * np.sin(Theta)
# fig,axes= plt.subplots(1,2, sharex=True, figsize=(10,5))
# sns.distplot(normal,ax=axes[0])
# axes[0].set_title('Normal Distribution')
# sns.distplot(X,ax=axes[1])
# axes[1].set_title('Box-Muller Algorithm')
# axes[0].set_facecolor('#EBEBEB')
# axes[1].set_facecolor('#EBEBEB')
# axes[0].grid(which='major', color='white', linewidth=1)
# axes[1].grid(which='major', color='white', linewidth=1)
# plt.show()


fig,axes= plt.subplots(figsize=(6,5))
sns.distplot(normal,ax=axes)
axes.set_title('numpy Normal Distribution')
axes.set_facecolor('#EBEBEB')
axes.grid(which='major', color='white', linewidth=1)

plt.xlim(-4.2, 4.2)
# plt.savefig('C:/Users/13862/Desktop/PDF_1.png')
plt.show()

fig,axes= plt.subplots(figsize=(6,5))
sns.distplot(X,ax=axes)
axes.set_title('Box-Muller Algorithm')
axes.set_facecolor('#EBEBEB')
axes.grid(which='major', color='white', linewidth=1)

plt.xlim(-4.2, 4.2)
# plt.savefig('C:/Users/13862/Desktop/PDF_2.png')
plt.show()


ks_statistic, p_value = kstest(normal, 'norm')
print(ks_statistic, p_value)
ks_statistic, p_value = kstest(X, 'norm')
print(ks_statistic, p_value)