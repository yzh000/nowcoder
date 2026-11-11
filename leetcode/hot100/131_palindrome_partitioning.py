"""
@Time ： 2026/10/15 17:04
@Auth ： seven
@File ：131_palindrome_partitioning.py
@IDE ：PyCharm
"""
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        path = []
        n = len(s)

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start):
            if start == n:
                ans.append(path[:])
                return

            for end in range(start + 1, n + 1):
                if is_palindrome(start, end):
                    sub = s[start : end]
                path.append(sub)
                backtrack(end)
                path.pop()
        backtrack(0)
        return ans