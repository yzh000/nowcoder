"""
@Time ： 2026/10/10 21:10
@Auth ： seven
@File ：98_validate_binary_search_tree.py
@IDE ：PyCharm
"""
class Solution:
    def isValidBST(self, root):
        def dfs(node, lower, upper):
            if node is None:
                return True

            if not (lower < node.val < upper):
                return False

            return (dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper))

        return dfs(root, float("-inf"), float("inf"))