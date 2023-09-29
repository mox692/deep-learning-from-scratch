import numpy as np
import matplotlib.pylab as plt

# 指数
def exp(x):
    return np.exp(x)

# sigmoid関数の定義: f(x) = 1 / e^(-x) + 1
def sigmoid(x):
    return 1 / (np.exp(-x) + 1)

print(exp(2)) # e^2 = 7.29....

print(sigmoid(0)) # 0.5
print(sigmoid(10000000)) # 1.0

# plot
x = np.arange(-4, 4, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.show()
