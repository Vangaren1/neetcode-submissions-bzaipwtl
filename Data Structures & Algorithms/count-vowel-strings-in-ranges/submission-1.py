class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")

        dp = [0]
        for word in words:
            word = word.lower()
            if word[0] in vowels and word[-1] in vowels:
                dp.append(dp[-1] + 1)
            else:
                dp.append(dp[-1])

        result = []

        for left, right in queries:
            result.append(dp[right + 1] - dp[left])
        return result