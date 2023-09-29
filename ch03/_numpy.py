import numpy as np

# numpy配列を

def double(a):
    return a * 2

# 違いを確認
print(double([1,2,3]))
print(double(np.array([1,2,3])))
