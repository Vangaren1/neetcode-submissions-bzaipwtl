# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, interval):
            if node is None:
                return True
            if node and (interval[0] >= node.val or interval[1] <= node.val):
                return False
            checkLeft = dfs(node.left, [interval[0], node.val])
            checkRight = dfs(node.right, [node.val, interval[1]])
            return checkLeft and checkRight

        return dfs(root, [float("-inf"), float("inf")])