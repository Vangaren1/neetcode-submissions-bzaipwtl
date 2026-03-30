# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, maximum):
            nonlocal count
            if node:
                if node.val >= maximum:
                    count += 1
                newMax = max(maximum, node.val)
                dfs(node.left, newMax)
                dfs(node.right, newMax)

        dfs(root, float("-inf"))
        return count