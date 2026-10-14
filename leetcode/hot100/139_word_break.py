"""
@Time ： 2026/10/13 21:14
@Auth ： seven
@File ：139_word_break.py
@IDE ：PyCharm
"""
class Solution:
    def wordBreak(self, s, wordDict) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n + 1):
            j = i
            while j >= 0:
                print(s[j : i])
                if s[j : i] in wordDict and dp[j] == True:
                    dp[i] = True
                    break
                j -= 1
        return dp[n]

