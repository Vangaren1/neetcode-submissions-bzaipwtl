class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lDict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        results = []

        def dfs(digits):
            if len(digits) == 0:
                return []
            if len(digits) == 1:
                return [d for d in lDict[digits]]
            results = []
            first = digits[0]
            remaining = self.letterCombinations(digits[1:])

            for f in lDict.get(first):
                for rem in remaining:
                    results.append(f + rem)

            return results

        return dfs(digits)