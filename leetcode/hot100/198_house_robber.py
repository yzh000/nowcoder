# LeetCode 198: house-robber
# https://leetcode.cn/problems/house-robber/
class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0], dp[1] = nums[0], nums[1]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[n - 1]


