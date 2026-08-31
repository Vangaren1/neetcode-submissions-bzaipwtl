class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")

        dp = []
        for word in words:
            word = word.lower()
            if word[0] in vowels and word[-1] in vowels:
                dp.append(1)
            else:
                dp.append(0)

        result = []

        for left, right in queries:
            totalVowels = 0
            for index in range(left, right + 1):
                totalVowels += dp[index]
            result.append(totalVowels)
        return result