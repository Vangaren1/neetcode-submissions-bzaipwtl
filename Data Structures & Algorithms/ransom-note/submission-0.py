class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = Counter(ransomNote)
        mc = Counter(magazine)

        for key, val in rc.items():
            if key not in mc or mc[key] < val:
                return False 
        return True