# LeetCode 46: permutations
# https://leetcode.cn/problems/permutations/
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        flag = [0] * n
        ans = []
        a = []
        def backtrack(temp):
            if len(temp) == n:
                ans.append(temp)
                temp = []
                for i in range(n):
                    if flag[i] == 0:
                        temp.append(nums[i])
                        flag[i] = 1
        backtrack(a)
        return ans

