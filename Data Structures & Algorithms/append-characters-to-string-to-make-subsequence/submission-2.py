class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0

        tPtr = 0

        for ch in s:
            if tPtr < len(t) and t[tPtr] == ch:
                tPtr += 1

        return len(t) - tPtr