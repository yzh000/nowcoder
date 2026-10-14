"""
@Time ： 2026/10/10 13:55
@Auth ： seven
@File ：二叉树层序遍历.py
@IDE ：PyCharm
"""
from collections import deque

def bfs(root):
    ans = []
    if not root:
        return []
    queue = deque(root)
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
        ans.append(level)
    return ans
