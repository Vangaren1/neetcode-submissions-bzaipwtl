import string
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = string.ascii_uppercase

        result = ""

        while columnNumber:
            columnNumber -= 1
            let = columnNumber % 26
            result += letters[let]
            columnNumber -= let
            columnNumber //= 26

        return result[::-1]