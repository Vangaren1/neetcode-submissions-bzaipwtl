class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        seen1 = {}
        seen2 = {}
        n = len(pattern)
        s = s.split()
        if len(s) != n:
            return False 
        for index in range(n):
            ch = pattern[index]
            word = s[index]
            if word in seen1 and seen1[word] != ch:
                return False 
            if ch in seen2 and seen2[ch] != word:
                return False
            seen1[word] = ch
            seen2[ch] = word
        return True 