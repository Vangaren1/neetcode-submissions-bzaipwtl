# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def trav(node):
            if node is None:
                return None 
             
            trav(node.left)
            result.append( node.val)
            trav(node.right)
        trav(root)
        return result

