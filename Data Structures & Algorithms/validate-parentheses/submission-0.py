class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pDict = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in ("[", "(", "{"):
                stk.append(c)
            elif c in ("]", ")", "}"):
                if len(stk) == 0:
                    return False
                if stk[-1] != pDict.get(c):
                    return False
                stk.pop()
        return len(stk) == 0