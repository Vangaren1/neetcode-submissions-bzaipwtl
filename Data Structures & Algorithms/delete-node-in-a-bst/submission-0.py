# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(node):
            if node is None:
                return None
            curr = node
            while curr.left:
                curr = curr.left
            return curr.val

        if root is None:
            return None

        if root.val == key:
            if root.left == None and root.right == None:
                return None
            if root.left == None and root.right:
                return root.right
            if root.left and root.right == None:
                return root.left
            m = findMin(root.right)
            root.right = self.deleteNode(root.right, m)
            root.val = m
            return root
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root    