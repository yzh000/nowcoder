# LeetCode 5: longest-palindromic-substring
# https://leetcode.cn/problems/longest-palindromic-substring/
from attr.validators import max_len


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j - i < 3:
                    if s[i] == s[j]:
                        if j - i < 3 or dp[i + 1][j - 1]:
                            dp[i][j] = True
                            if j - i + 1 > max_len:
                                start = i
                                max_len = j - i + 1

        return start[start:start + max_len]
