class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for index in range(len(s) + 1):
            for word in wordDict:
                tmp = len(word) + index
                subString = s[index:tmp]
                if subString == word:
                    dp[tmp] = dp[index] or dp[tmp]
        return dp[-1]