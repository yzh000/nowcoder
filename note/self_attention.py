"""
@Time ： 2026/10/19 22:20
@Auth ： seven
@File ：self_attention.py
@IDE ：PyCharm
"""
import numpy as np
from transformers.models.cvt.convert_cvt_original_pytorch_checkpoint_to_pytorch import attention


def sofmax(x):
    x = x - np.max(
        x,
        axis=-1,
        keepdims=True
    )
    exp_x = np.exp(x)
    return exp_x / np.sum(
        exp_x,
        axis=-1,
        keepdims=True
    )

class SelfAttention:
    def __init__(self, d_model):
        self.d_model = d_model

        self.Wq = np.random.randn(d_model, d_model)
        self.Wk = np.random.randn(d_model, d_model)
        self.Wv = np.random.randn(d_model, d_model)

    def forward(self, X):
        # 1. 生成 Q K V
        Q = X @ self.Wq
        K = X @ self.Wk
        V = X @ self.Wv

        # 2. QK^T
        scores = Q @ K.T

        # 3. Scaling
        scores = scores / np.sqrt(self.d_model)

        # 4. Softmax
        attention = sofmax(scores)

        # 5. 加权 V

        output = attention @ V

        return output

if __name__ == "__main__":
    seq_len = 4
    d_model = 8

    X = np.random.randn(seq_len, d_model)

    model = SelfAttention(d_model)

    output = model.forward(X)

    print(output.shape)