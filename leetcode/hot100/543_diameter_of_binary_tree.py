"""
@Time ： 2026/10/10 13:10
@Auth ： seven
@File ：543_diameter_of_binary_tree.py
@IDE ：PyCharm
"""
class Solution:
    def diameterOfBinaryTree(self, root):
        ans = 0
        def depth(node):
            nonlocal ans
            if node is None:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            ans = max(ans, left + right)

            return max(left, right) + 1
        depth(root)
        return ans

