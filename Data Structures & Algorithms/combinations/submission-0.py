class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(index: int, curr: list):
            if len(curr) == k:
                results.append(curr)
                return
            if index > n:
                return

            last = -1

            if len(curr) > 0:
                last = curr[-1]

            if last != index:
                curr.append(index)

                dfs(index, curr.copy())
                curr.pop()
            dfs(index + 1, curr)

        dfs(1, [])
        return results