class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        largest = ""
        lInt = -1
        for index in range(n-2):
            curr = num[index:index+3]

            if curr[0] == curr[1] and curr[1] == curr[2] and int(curr) > lInt:
                largest = curr
                lInt = int(curr)
        return largest