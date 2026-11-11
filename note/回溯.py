"""
@Time ： 2026/10/15 17:14
@Auth ： seven
@File ：回溯.py
@IDE ：PyCharm
"""
# 选择
#  ↓
# 递归
#  ↓
# 撤销
#
# LC 46 全排列
# LC 78 子集
# LC 39 组合总和
# LC 22 括号生成
# LC 51 N皇后
#
# 牛客 BM55 没有重复项数字的全排列
#
# ans = []
# path = []
#
# def backtrack(...):
#     if 结束条件:
#         ans.append(path[:])
#     if 选择 in 选择列表:
#         #做选择
#         path.append(选择)
#         backtrack(...)
#         # 撤销选择
#         path.pop()