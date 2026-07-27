"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def recur(n, offsetY, offsetX):
            if n == 1:
                v = grid[offsetY][offsetX]
                return Node(v, True, None, None, None, None)

            newN = n // 2
            topLeft = recur(newN, offsetY, offsetX)
            topRight = recur(newN, offsetY, offsetX + newN)
            bottomLeft = recur(newN, offsetY + newN, offsetX)
            bottomRight = recur(newN, offsetY + newN, offsetX + newN)
            total = topLeft.val + topRight.val + bottomLeft.val + bottomRight.val

            newVal = 0
            if (
                total in (0, 4)
                and topLeft.isLeaf
                and topRight.isLeaf
                and bottomLeft.isLeaf
                and bottomRight.isLeaf
            ):
                newVal = 0 if total == 0 else 1

                return Node(newVal, True, None, None, None, None)

            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)

        n = len(grid)
        return recur(n, 0, 0)