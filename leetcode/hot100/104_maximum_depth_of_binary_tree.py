"""
@Time ： 2026/10/10 13:19
@Auth ： seven
@File ：104_maximum_depth_of_binary_tree.py
@IDE ：PyCharm
"""
class Solution:
    def maxDepth(self, root):
        def depth(node):
            nonlocal ans
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            return max(left, right) + 1
        ans = depth(root)
        print(ans)