class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(index: int, curr: list):
            if len(curr) == k:
                results.append(curr.copy())
                return
            if index > n:
                return

            curr.append(index)
            dfs(index + 1, curr)
            curr.pop()
            dfs(index + 1, curr)

        dfs(1, [])
        return results