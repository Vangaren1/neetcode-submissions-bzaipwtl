class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:

        originalEdges = edges[:]
        # build the MST
        edges.sort(key=lambda x: x[2])

        def getCost(index, useSkip=True, forceInclude=None):
            quMap = QU(n)
            include = []
            totalWeight = 0
            skipA, skipB, _ = originalEdges[index]

            if forceInclude:
                a, b, w = originalEdges[index]
                quMap.union(a, b)
                totalWeight += w

            for pointA, pointB, weight in edges:
                if useSkip and pointA == skipA and pointB == skipB:
                    continue
                if quMap.find(pointA) == quMap.find(pointB):
                    continue
                quMap.union(pointA, pointB)
                include.append((pointA, pointB, weight))
                totalWeight += weight

            return (totalWeight, quMap.components)

        originalMST = getCost(0, useSkip=False)
        print(originalMST)

        critical, pseudo = [], []

        for index in range(len(edges)):
            weight, components = getCost(index)
            if weight > originalMST[0] or components > originalMST[1]:
                critical.append(index)
                continue

            weight, components = getCost(index, useSkip=False, forceInclude=True)
            if weight == originalMST[0] and originalMST[1] == components:
                pseudo.append(index)

        return [critical, pseudo]


class QU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.components = n

    def find(self, n):
        while self.parents[n] != n:
            n = self.parents[n]
        return n

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA == rootB:
            return False

        if self.size[rootA] < self.size[rootB]:
            rootA, rootB = rootB, rootA
        self.parents[rootB] = rootA
        self.size[rootA] += self.size[rootB]
        self.components -= 1