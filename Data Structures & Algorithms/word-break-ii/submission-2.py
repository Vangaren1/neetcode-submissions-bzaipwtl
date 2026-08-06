class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        results = []
        words = set(wordDict)
        n = len(s)
        curr = []

        def backtrack(index):
            if index == n:
                results.append(" ".join(curr))
                return 

            for word in words:
                if word != s[index : len(word) + index]:
                    continue

                curr.append(word)
                backtrack(index + len(word))

                curr.pop()

        backtrack(0)
        return results