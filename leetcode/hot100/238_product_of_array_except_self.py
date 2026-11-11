# LeetCode 238: product-of-array-except-self
# https://leetcode.cn/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums) -> [int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        ans = []
        for i in range (1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        for i in range(n):
            cur = prefix[i] * postfix[i]
            ans.append(cur)
        return ans
