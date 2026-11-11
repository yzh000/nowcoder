# LeetCode 153: find-minimum-in-rotated-sorted-array
# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        if nums[left] <= nums[right]:
            return nums[left]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
              right = mid
            else:
                left = mid + 1
            if left == right:
                return nums[left]

