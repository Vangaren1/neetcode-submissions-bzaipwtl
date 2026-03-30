class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        results = set()

        def dfs(curr, index, total):
            if total == target:
                results.add(tuple(curr.copy()))
                return

            if index >= len(candidates):
                return

            curr.append(candidates[index])
            dfs(curr, index + 1, total + candidates[index])
            curr.pop()
            dfs(curr, index + 1, total)

        dfs([], 0, 0)
        return [[i for i in r] for r in results]