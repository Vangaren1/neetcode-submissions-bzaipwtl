class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s==t:
            return True
        if  len(s)>len(t):
            return False
        sPtr = 0
        
        for ch in t:
            if sPtr < len(s) and s[sPtr] == ch:
                sPtr+= 1
            if sPtr == len(s):
                return True
        
        return False 