# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # return (canRob, cantRob)
        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            canRob = node.val + left[1] + right[1]
            dontRob = max(left) + max(right)

            return (canRob, dontRob)

        return max(dfs(root))