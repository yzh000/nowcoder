"""
@Time ： 2026/10/10 12:18
@Auth ： seven
@File ：isSymmetric.py
@IDE ：PyCharm
"""
"""
重点：交叉递归比较
"""
import ast
from collections import deque


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def build_tree(nums):
    if not nums or nums[0] is None:
        return None
    root = TreeNode(nums[0])
    queue = deque([root])

    i = 1

    while queue and i < len(nums):
        node = queue.popleft()

        if i < len(nums) and nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)

        i += 1

        if i < len(nums) and nums[i] is not None:
            node.right = TreeNode(nums[i])
            queue.append(node.right)

        i += 1

    return root


def solve():
    nums = ast.literal_eval(input().strip())
    root = build_tree(nums)
    result = isSymmetric(root)
    print("true" if result else "false")


def isSymmetric(self, root):
    def check(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        return (
                left.val == right.val
                and check(left.left, right.right)
                and check(left.right, right.left)
        )

    if root is None:
        return True
    return check(root.left, root.right)
