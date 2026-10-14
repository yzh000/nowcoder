"""
@Time ： 2026/10/13 20:49
@Auth ： seven
@File ：哈希表.py
@IDE ：PyCharm
"""
"""
典型关键词：
    出现次数、有没有出现、快速查找、两数之和
    本质：用O(n)的空间复杂度，换O(1)查询
    典型题:
        LC 1 两数之和
        LC 49 字母异位词分组
        LC 128 最长连续序列
        LC 347 前K个高频元素
"""
def two_sum(nums, target):
    pos = {}

    for i, x in enumerate(nums):
        need = target - x
        if need in pos:
            return pos[need], i
        pos[x] = i
    return -1, -1

if __name__ == "__main__":
    n, target = map(int, input().split())
    nums = list(map(int, input().split()))

    i, j = two_sum(nums, target)
    print(i, j)

