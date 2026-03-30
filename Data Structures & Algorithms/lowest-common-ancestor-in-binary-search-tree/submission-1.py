# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ptr = root

        while True:
            if ptr.val < p.val and ptr.val < q.val:
                ptr = ptr.right
            elif ptr.val > p.val and ptr.val > q.val:
                ptr = ptr.left
            else:
                return ptr