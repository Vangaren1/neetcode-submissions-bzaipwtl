# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        maxFound = float("-inf")

        def dfs(node):
            nonlocal maxFound
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            allowToSplit = left + right + node.val
            maxChild = max(left, right, 0)
            maxFound = max(maxFound, allowToSplit, node.val, node.val + maxChild)
            return node.val + maxChild

        dfs(root)

        return maxFound