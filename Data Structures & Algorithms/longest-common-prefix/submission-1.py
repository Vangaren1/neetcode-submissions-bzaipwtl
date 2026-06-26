class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 1:
            return strs[0]
        n = min(len(s) for s in strs)
        for i in range(n):
            tmp = strs[1:]
            for s in tmp:
                if s[i] != strs[0][i]:
                    return prefix
            prefix += strs[1][i]
        return prefix