"""
@Time ： 2026/10/12 15:50
@Auth ： seven
@File ：739_daily_temperatures.py
@IDE ：PyCharm
"""
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[stack[i]] > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans

