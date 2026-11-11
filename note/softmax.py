"""
@Time ： 2026/10/19 22:18
@Auth ： seven
@File ：softmax.py
@IDE ：PyCharm
"""
import numpy as np

def softmax(x):
    x = x - np.max(x)

    exp_x = np.exp(x)

    return exp_x / np.sum(exp_x)

if __name__ == "__main__":
    x = np.array([1.0, 2.0, 3.0])
    print(softmax(x))