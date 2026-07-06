class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1, ptr2 = 0, 0
        result = ""
        while ptr1 < len(word1) and ptr2 < len(word2):
            result += word1[ptr1]
            result += word2[ptr2]
            ptr1 += 1
            ptr2 += 1

        if ptr1 < len(word1):
            return result + word1[ptr1:]
        return result + word2[ptr2:]