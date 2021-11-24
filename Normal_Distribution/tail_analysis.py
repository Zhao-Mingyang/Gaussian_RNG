import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
sns.set()
import warnings
warnings.simplefilter("ignore", UserWarning)



# Tail analysis_______________________________________
normal = np.array([0 for i in range(1000000)], dtype=np.longdouble)
bm = np.array([0 for i in range(1000000)], dtype=np.longdouble)

for i in range(1000000):
    n = np.random.randn()
    while(n<3.90):
        n = np.random.randn()
    normal[i] = n

for i in range(1000000):
    U1 = np.random.uniform()
    U2 = np.random.uniform()
    R = np.sqrt(-2 * np.log(U1))
    Theta = 2 * np.pi * U2
    X = R * np.cos(Theta)
    while(X<3.90):
        U1 = np.random.uniform()
        U2 = np.random.uniform()
        R = np.sqrt(-2 * np.log(U1))
        Theta = 2 * np.pi * U2
        X = R * np.cos(Theta)
    bm[i] = n

fig,axes= plt.subplots(figsize=(6,5))
sns.distplot(normal,ax=axes)
axes.set_title('numpy Normal Distribution Tail')
axes.set_facecolor('#EBEBEB')
axes.grid(which='major', color='white', linewidth=1)

# plt.xlim(-4.2, 4.2)
# plt.savefig('C:/Users/13862/Desktop/PDF_1.png')
plt.show()

fig,axes= plt.subplots(figsize=(6,5))
sns.distplot(bm,ax=axes)
axes.set_title('Box-Muller Algorithm Tail')
axes.set_facecolor('#EBEBEB')
axes.grid(which='major', color='white', linewidth=1)

# plt.xlim(-4.2, 4.2)
# plt.savefig('C:/Users/13862/Desktop/PDF_2.png')
plt.show()
