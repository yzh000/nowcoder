# LeetCode 322: coin-change
# https://leetcode.cn/problems/coin-change/
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        dp = [-1] * (amount + 1)
        dp[0] = 0
        if amount == 0:
            return 0
        for i in range(1, amount + 1):
            for j in range(n):
                if coins[j] > i:
                    continue
                if dp[i - coins[j]] == -1:
                    continue
                candidate = dp[i - coins[j]] + 1
                if dp[i] == -1:
                    dp[i] = candidate
                else:
                    dp[i] = min(dp[i], candidate)
        return dp[amount]
