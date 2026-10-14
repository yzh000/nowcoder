"""
@Time ： 2026/10/10 18:38
@Auth ： seven
@File ：347_top_k_frequent_elements.py
@IDE ：PyCharm
"""
import random
from collections import Counter


class Solution1:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        def partition(left, right):
            random_index = random.randint(left, right)
            a[random_index], a[right] = a[right], a[random_index]
            pivot = a[right]
            p = left
            for i in range(left, right):
                if a[i] <= pivot:
                    a[i], a[p] = a[p], a[i]
                    p += 1
            a[p], a[right] = a[right], a[p]
            return p
        a = []
        count = Counter(nums)
        a = list(count.keys())

        left = 0
        right = len(a) - 1
        target = k

        while left <= right:
            p = partition(left, right, a)
            if target == p:
                break
            elif p > target:
                right = p - 1

            else:
                left = p + 1
        return a[target:]




class Solution2:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            bucket[freq].append(num)

        ans = []

        for freq in range(len(nums), 0, -1):
            for num in bucket[freq]:
                ans.append(num)
                if len(ans) == k:
                    return ans