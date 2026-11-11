# LeetCode 11: container-with-most-water
# https://leetcode.cn/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        ans = 0
        while left < right:
            temp = min(height[left], height[right])
            ans = max(ans, temp * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans

