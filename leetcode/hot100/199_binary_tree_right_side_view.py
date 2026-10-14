"""
@Time ： 2026/10/10 14:48
@Auth ： seven
@File ：199_binary_tree_right_side_view.py.py
@IDE ：PyCharm
"""
from collections import deque
class Solution:
    def rightSideView(self,root):
        ans = []
        if root is None:
            return []
        queue = deque(root)
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(node.val)
        return ans

