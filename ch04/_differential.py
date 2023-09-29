import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定義域を設定します
x1 = np.linspace(-5, 5, 100)  # x1の範囲と分割数を指定
x2 = np.linspace(-5, 5, 100)  # x2の範囲と分割数を指定

X1, X2 = np.meshgrid(x1, x2)  # x1とx2の格子点を生成
Y = X1**2 + X2**2  # 2変数関数の定義

# プロットします
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, X2, Y, cmap='viridis')  # 3Dプロット

ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')

plt.show()
