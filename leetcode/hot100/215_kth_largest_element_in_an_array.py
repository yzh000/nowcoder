"""
@Time ： 2026/10/10 15:00
@Auth ： seven
@File ：215_kth_largest_element_in_an_array.py
@IDE ：PyCharm
"""


import random
import heapq

class Solution1:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # 第 k 大 = 升序排列后下标 n-k
        target = len(nums) - k

        left = 0
        right = len(nums) - 1

        while left <= right:
            # 随机选择 pivot
            pivot = nums[random.randint(left, right)]

            # 三路划分
            lt = left
            i = left
            gt = right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1

                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1

                else:
                    i += 1

            # 此时：
            # [left, lt-1] < pivot
            # [lt, gt] == pivot
            # [gt+1, right] > pivot

            if target < lt:
                right = lt - 1

            elif target > gt:
                left = gt + 1

            else:
                return pivot

class Solution2:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

            return heap[0]