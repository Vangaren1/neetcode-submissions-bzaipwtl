class Solution:
    def romanToInt(self, s: str) -> int:
        rDict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
              
        odd = {
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        total = 0
        
        if len(s) == 0:
            return 0
        
        ptr = 0
        while ptr < len(s):
            curr = s[ptr]
            next = ''
            if ptr < len(s)-1:
                next = s[ptr+1]
            if curr+next in odd.keys():
                total += odd[curr+next]
                ptr += 2
            else:
                total += rDict[curr]
                ptr += 1 
        return total