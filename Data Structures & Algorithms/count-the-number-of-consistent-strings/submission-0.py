class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        good = set(allowed)

        count = 0 
        for word in words:
            ok = True
            for ch in word:
                if ch not in good:
                    ok = False
            if ok:
                count += 1
        return count 
        