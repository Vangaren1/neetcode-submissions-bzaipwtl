# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            # if the root is None, then it's a empty branch
            if root is None:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            self.maximum = max(self.maximum, left + right + 2)
            return 1 + max(left, right)

        self.maximum = 0
        dfs(root)
        return self.maximum