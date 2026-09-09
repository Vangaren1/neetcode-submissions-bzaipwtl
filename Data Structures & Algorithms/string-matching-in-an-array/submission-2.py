class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = set()
        wset = set(words)
        for word1 in wset:
            for word2 in wset:
                if word1 == word2:
                    continue
                if word1 in word2:
                    output.add(word1)
        return [ o for o in output]