class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for ch in s1:
            d1[ch] += 1

        # advance ptr2 to the length of s1
        ptr1 = 0
        ptr2 = 0
        while ptr2 < len(s1):
            d2[s2[ptr2]] += 1
            ptr2 += 1

        if d1 == d2:
            return True

        while ptr2 < len(s2):
            # subtract the character at ptr1's position
            d2[s2[ptr1]] -= 1
            if d2[s2[ptr1]] == 0:
                d2.pop(s2[ptr1])
            # increment ptr2 character
            d2[s2[ptr2]] += 1
            # check if dictionaries match
            if d1 == d2:
                return True
            # increment pointers
            ptr1 += 1
            ptr2 += 1

        return False