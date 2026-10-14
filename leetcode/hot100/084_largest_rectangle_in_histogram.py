"""
@Time ： 2026/10/13 15:04
@Auth ： seven
@File ：084_largest_rectangle_in_histogram.py
@IDE ：PyCharm
"""
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [-1]
        n = len(heights)
        ans = 0
        for i in range(n):
            cur = 0 if i == n else heights[i]
            while stack[-1] != -1 and heights[stack[-1]] >= cur:
                h = heights[stack.pop()]
                width = i - stack[-1] - 1
                ans = max(ans, h * width)
            stack.append(i)
        return ans