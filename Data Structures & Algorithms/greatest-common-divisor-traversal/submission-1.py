class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)

        uf = self.UnionFind(n)

        def factor(number):
            found = set()
            d = 2

            while d * d <= number:
                if number % d == 0:
                    found.add(d)

                    while number % d == 0:
                        number //= d

                d += 1

            if number > 1:
                found.add(number)

            return found

        f = [factor(i) for i in nums]

        factMap = defaultdict(list)
        for index, fmap in enumerate(f):
            for fact in fmap:
                factMap[fact].append(index)

        for key, val in factMap.items():
            if len(val) > 1:
                for v in val[1:]:
                    uf.union(val[0], v)

        return uf.components == 1

    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
            self.components = n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])  # path compression
            return self.parent[x]

        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False

            # weighted union
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
            self.components -= 1
            return True