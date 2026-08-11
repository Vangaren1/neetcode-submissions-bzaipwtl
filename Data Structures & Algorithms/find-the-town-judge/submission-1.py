class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [set() for _ in range(n + 1)]
        trusts = [set() for _ in range(n + 1)]

        for a, b in trust:
            trusted[b].add(a)
            trusts[a].add(b)

        for index in range(n+1):
            if len(trusted[index]) == n - 1 and len(trusts[index]) == 0:
                return index
        return -1