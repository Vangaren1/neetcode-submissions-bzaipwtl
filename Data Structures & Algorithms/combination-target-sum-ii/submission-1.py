class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        results = []

        def dfs(curr, index, total):
            if total == target:
                results.append(curr.copy())
                return

            if index >= len(candidates) or total > target:
                return

            # include element at index
            curr.append(candidates[index])
            dfs(curr, index + 1, total + candidates[index])
            curr.pop()
            while (
                index < len(candidates) - 1
                and candidates[index] == candidates[index + 1]
            ):
                index += 1
            dfs(curr, index + 1, total)

        dfs([], 0, 0)
        return results