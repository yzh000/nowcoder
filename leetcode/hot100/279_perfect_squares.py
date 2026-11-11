# LeetCode 279: perfect-squares
# https://leetcode.cn/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = i
            for j in range(i):
                if j * j > i:
                    break
                dp[i] = min(dp[i - j] + dp[i - j * j], dp[i])
        return dp[n]