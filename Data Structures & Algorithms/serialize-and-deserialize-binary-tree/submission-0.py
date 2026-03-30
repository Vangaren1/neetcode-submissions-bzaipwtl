# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodes = []

        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr:
                nodes.append(str(curr.val)) if curr != "N" else nodes.append("N")
                if curr != "N":
                    queue.append(curr.left) if curr.left else queue.append("N")
                    queue.append(curr.right) if curr.right else queue.append("N")

        while nodes and nodes[-1] == "N":
            nodes.pop()

        return "/".join(nodes)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
        nodes = data.split("/")

        nodes = [int(n) if n != "N" else None for n in nodes]
        print(nodes)

        if len(nodes) == 0:
            return None

        root = TreeNode(nodes.pop(0))
        queue = [root]
        while queue:
            curr = queue.pop(0)

            if nodes:
                left = nodes.pop(0)
                if left:
                    curr.left = TreeNode(left)
                    queue.append(curr.left)

            if nodes:
                right = nodes.pop(0)
                if right:
                    curr.right = TreeNode(right)
                    queue.append(curr.right)

        return root