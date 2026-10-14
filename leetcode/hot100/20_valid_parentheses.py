"""
@Time ： 2026/10/12 15:43
@Auth ： seven
@File ：20_valid_parentheses.py
@IDE ：PyCharm
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False

                stack.pop()

            else:
                stack.append(ch)

        return len(stack) == 0
