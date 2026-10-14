"""
@Time ： 2026/10/10 13:28
@Auth ： seven
@File ：102_binary_tree_level_order_traversal.py
@IDE ：PyCharm
"""
from collections import deque
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        queue = deque([root])
        ans = []

        while queue:
            size = len(queue)
            level = []

            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(queue)
        return ans
