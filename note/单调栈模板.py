"""
@Time ： 2026/10/13 21:08
@Auth ： seven
@File ：单调栈模板.py
@IDE ：PyCharm
"""
# 核心口诀：
# 什么时候答案被当前元素确定，什么时候弹栈。
# stack = []
#
# for i in range(len(nums)):
#
#     while stack and nums[i] < nums[stack[-1]]:
#         idx = stack.pop()
#         # nums[i] 是 nums[idx] 右边第一个更小元素
#
#     stack.append(i)