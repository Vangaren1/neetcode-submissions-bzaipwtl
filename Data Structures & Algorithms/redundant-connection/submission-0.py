class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mA, mB = max([a[0] for a in edges]), max([b[1] for b in edges])
        qu = self.QUFind(max(mA, mB)+1)
        for a, b in edges:
            check = qu.union(a, b)
            if not check:
                return [a, b]

    class QUFind:
        def __init__(self, n):
            self.array = [i for i in range(n)]

        def connected(self, a, b):
            return self.array[a] == self.array[b]

        def union(self, a, b):
            currA = self.array[a]
            currB = self.array[b]
            if currA == currB:
                return False
            for index in range(len(self.array)):
                if self.array[index] == currA:
                    self.array[index] = currB
            return True