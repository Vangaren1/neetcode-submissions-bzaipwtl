class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}

        if (len(s1) + len(s2)) != len(s3):
            return False

        def recur(index1, index2):
            index3 = index1 + index2
            if (index1, index2) in cache:
                return cache[(index1, index2)]
            if index3 == len(s3):
                return index1 == len(s1) and index2 == len(s2)

            check = False
            if index1 < len(s1) and s1[index1] == s3[index3]:
                check = recur(index1 + 1, index2)
                if check:
                    cache[(index1, index2)] = True
                    return True
            if index2 < len(s2) and s2[index2] == s3[index3]:
                check = recur(index1, index2 + 1)
                if check:
                    cache[(index1, index2)] = True
                    return True
            cache[(index1, index2)] = False
            return False

        return recur(0, 0)