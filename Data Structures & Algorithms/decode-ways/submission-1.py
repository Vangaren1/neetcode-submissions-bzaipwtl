class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dfs(substring):
            if len(substring) == 0:
                return 1
            if substring[0] == "0":
                return 0
            if len(substring) == 1:
                return 1
            secondAlso = substring[:2]
            if int(secondAlso) > 26:
                secondAlso = None
            total = dfs(substring[1:])
            if secondAlso:
                total += dfs(substring[2:])
            return total

        return dfs(s)