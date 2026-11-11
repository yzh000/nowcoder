"""
@Time ： 2026/10/18 20:07
@Auth ： seven
@File ：1800_max_ascending_sum.py
@IDE ：PyCharm
"""
class Solution:
    def maxAscendingSum(self, nums) -> int:
        n = len(nums)
        ans = 0
        cur = 0
        pre = 0
        for i in range(n):
            if nums[i] > pre:
                cur += nums[i]
                pre = nums[i]
            else:
                ans = max(ans, cur)
                cur = nums[i]
                pre = nums[i]
        ans = max(ans, cur)
        return ans
