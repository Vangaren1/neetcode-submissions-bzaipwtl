class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        partition = []

        def dfs(index):
            if index >= len(s):
                results.append(partition.copy())
                return

            for j in range(index, len(s)):
                if self.isPalindrome(s[index : j + 1]):
                    partition.append(s[index : j + 1])
                    dfs(j + 1)
                    partition.pop()

        dfs(0)

        return results

    def isPalindrome(self, s: str) -> bool:
        head = 0
        tail = len(s) - 1
        while head < tail:
            if s[head] != s[tail]:
                return False
            head += 1
            tail -= 1
        return True

