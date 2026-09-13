class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def isomap(st):
            start = 0 
            seen = {}
            results = []
            for ch in st:
                if ch not in seen:
                    seen[ch] = start
                    start += 1
                results.append(seen[ch])
            return results 
        
        map1 = isomap(s)
        map2 = isomap(t)
        
        for index in range(len(map1)):
            if map1[index] != map2[index]:
                return False
        return True 