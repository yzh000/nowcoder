"""
@Time ： 2026/10/17 20:47
@Auth ： seven
@File ：dual_config_training_dp.py
@IDE ：PyCharm
"""
import sys
def solve():
    input = sys.stdin.readline
    n, C = map(int, input().split())

    tasks = []
    for _ in range(n):
        c1, t1, c2, t2 = map(int, input().split())
        tasks.append((c1, t1, c2, t2))
    INF = float("inf")
    dp = [INF] * (C + 1)
    dp[0] = 0
    for c1, t1, c2, t2 in tasks:
        ndp = [INF] * (C + 1)

        for used in range(C + 1):
            if dp[used] == INF:
                continue
            if used + c1 <= C:
                ndp[used + c1] = min(ndp[used + c1], dp[used] + t1)
            if used + c2 <= C:
                ndp[used + c2] = min(ndp[used + c2], dp[used] + t2)

        dp = ndp

        min_time = min(dp)

    for i in range(C + 1):
        if dp[i] == min_time:
            used_resource = i
            break

    remain_resource = C - used_resource
    print(min_time, used_resource, remain_resource)

if __name__ == "__main__":
    solve()
