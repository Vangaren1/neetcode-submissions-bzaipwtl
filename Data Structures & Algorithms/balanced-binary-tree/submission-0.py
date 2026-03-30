# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    heights = {}

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def height(node: TreeNode):
            if node is None:
                return 0
            self.heights[node] = 1 + max(height(node.left), height(node.right))
            return self.heights[node]

        leftH = height(root.left)
        rightH = height(root.right)

        heightBalanced = abs(leftH - rightH) <= 1

        leftBalanced = self.isBalanced(root.left)
        rightBalanced = self.isBalanced(root.right)

        return heightBalanced and leftBalanced and rightBalanced