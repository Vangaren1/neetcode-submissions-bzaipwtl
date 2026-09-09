class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = set()

        for word1 in words:
            for word2 in words:
                if word1 == word2:
                    continue
                if word1 in word2:
                    output.add(word1)
        return [ o for o in output]