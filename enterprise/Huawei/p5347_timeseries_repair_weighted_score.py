"""
@Time ： 2026/10/11 13:37
@Auth ： seven
@File ：p5347_timeseries_repair_weighted_score.py
@IDE ：PyCharm
"""
import sys
import math

from Demos.mmapfile_demo import offset


def solve():
    # data = list(map(int, sys.stdin.buffer.read().split()))
    # if not data:
    #     return
    #
    # it = iter(data)
    #
    # n = next(it)
    # w = next(it)
    # k = next(it)
    #
    # t = [0] * n
    # v = [0] * n
    # q = [0] * n
    #
    # for i in range(n):
    #     t[i] = next(it)
    #     v[i] = next(it)
    #     q[i] = next(it)


    n, w, k = map(int, input().split())

    t = [0] * n
    v = [0] * n
    q = [0] * n

    for i in range(n):
        t[i], v[i], q[i] = map(int, input().split())
    # =========================================================
    # 阶段一：修复 q = 2 的无效数据
    # =========================================================

    left = [-1] * n

    last_valid = -1

    for i in range(n):
        left[i] = last_valid

        if q[i] == 0:
            last_valid = i

    right = [-1] * n

    last_valid = -1

    for i in range(n - 1, -1, -1):
        right[i] = last_valid

        if q[i] == 0:
            last_valid = i

    # a：第一阶段修复后的数组

    a = [float(x) for x in v]

    for i in range(n):
        if q[i] != 2:
            continue

        l = left[i]
        r = right[i]

        # 左右都有有效数据
        if l != -1 and r != -1:
            a[i] = (
                    v[l]
                    + (v[r] - v[l])
                    * (t[i] - t[l]) / (t[r] - t[l])
            )

        # 只有左边
        elif l != -1:
            a[i] = float(v[l])
        # 只有右边
        elif r != -1:
            a[i] = float(v[r])
        # 左右都没有
        else:
            a[i] = float(v[i])

    # =========================================================
    # 阶段二：局部异常处理
    # =========================================================
    h = (w - 1) // 2

    # 为减少大数计算方差时的浮点误差，
    # 先整体平移一个 offset。
    offset = math.fsum(a) / n

    # prefix：
    # (a[i] - offset) 的前缀和

    prefix = [0.0] * (n + 1)
    # prefix_sq：
    # (a[i] - offset)^2 的前缀和

    prefix_sq = [0.0] * (n + 1)

    for i in range(n):
        x = a[i] - offset
        prefix[i + 1] = prefix[i] + x
        prefix_sq[i + 1] = prefix_sq[i] + x * x

    b = [0.0] * n

    for i in range(n):

        # 当前窗口左右边界
        L = max(0, i - h)
        R = min(n - 1, i + h)

        cnt = R - L + 1
        # 窗口内平移后的和
        window_sum = prefix[R + 1] - prefix[L]
        # 窗口内平移后的平方和
        window_sq_sum = prefix_sq[R + 1] - prefix_sq[L]

        # 平移后的均值
        mean_shift = window_sum / cnt
        # 原始均值
        mu = offset + mean_shift

        # Var(X) = E(X^2) - E(X)^2

        variance = (window_sq_sum / cnt) - (mean_shift * mean_shift)

        # 防止浮点误差导致 variance 出现极小负数

        variance = max(0.0, variance)

        sigma = math.sqrt(variance)

        # 判断是否为局部异常值

        if abs(a[i] - mu) > k * sigma:
            b[i] = mu

        else:
            b[i] = a[i]

    # =========================================================
    # 阶段三：z-score 标准化
    # =========================================================

    mean_b = math.fsum(b) / n

    variance_b = (
            math.fsum(
                (x - mean_b) ** 2 for x in b
            ) / n
    )

    s = math.sqrt(max(0.0, variance_b))

    # 所有值相同
    if s == 0.0:
        print(0)
        return

    # =========================================================
    # 阶段四：质量加权
    # =========================================================

    # q -> p
    quality_weight = (
        1.0,
        0.5,
        0.25
    )

    denominator = 0.0
    numerator = 0.0

    for i in range(n):
        p = quality_weight[q[i]]
        value_weight = p * abs(b[i])

        denominator += value_weight
        z_abs = abs((b[i] - mean_b) / s)
        numerator += value_weight * z_abs

    # 理论上 denominator=0 时所有 b[i] 都为 0，
    # 此时最终得分定义为 0。

    if denominator == 0.0:
        print(0)
        return

    score = numerator / denominator

    # =========================================================
    # 四舍五入
    # =========================================================
    # 注意：
    # Python 的 round() 是“银行家舍入”，
    # 题目要求普通四舍五入。

    ans = math.floor(score * 100 + 0.5)

    print(ans)


if __name__ == "__main__":
    solve()
