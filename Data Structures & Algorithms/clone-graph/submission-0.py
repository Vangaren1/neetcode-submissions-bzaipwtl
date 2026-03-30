"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneDict = {}

        def dfs(n: Optional["Node"]):
            if n is None:
                return None
            if n in cloneDict.values():
                return n
            if n in cloneDict:
                return cloneDict[n]
            cloneDict[n] = Node(n.val)
            if n.neighbors:
                for neigh in n.neighbors:
                    newNeighbor = dfs(neigh)
                    cloneDict[n].neighbors.append(newNeighbor)
            return cloneDict[n]

        return dfs(node)