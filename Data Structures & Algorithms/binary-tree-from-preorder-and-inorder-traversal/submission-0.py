# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder and inorder:
            root = TreeNode(preorder.pop(0))

            index = 0
            while inorder[index] != root.val:
                index += 1

            left = inorder[0:index]
            right = inorder[index + 1 :]

            leftPre = []
            for _ in range(len(left)):
                leftPre.append(preorder.pop(0))

            rightPre = preorder

            root.left = self.buildTree(leftPre, left)
            root.right = self.buildTree(rightPre, right)

            return root