class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0

        dp = {}  # (idx, idx) -> num

        def recursive(index1, index2):
            if (index1, index2) in dp:
                return dp[(index1, index2)]
            if index1 == len(word1):
                dp[(index1, index2)] = abs(len(word2) - index2)
                return dp[(index1, index2)]
            if index2 == len(word2):
                dp[(index1, index2)] = abs(len(word1) - index1)
                return dp[(index1, index2)]

            if word1[index1] == word2[index2]:
                return recursive(index1 + 1, index2 + 1)

            insert1 = 1 + recursive(index1 + 1, index2)
            delete1 = 1 + recursive(index1, index2 + 1)
            swap = 1 + recursive(index1 + 1, index2 + 1)
            dp[(index1, index2)] = min(insert1, delete1, swap)
            return dp[(index1, index2)]

        return recursive(0, 0)