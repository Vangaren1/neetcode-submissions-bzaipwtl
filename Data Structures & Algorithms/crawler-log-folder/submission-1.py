class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = 0

        for log in logs:
            if log == '../':
                if stk > 0:
                    stk -=1
                else:
                    continue
            elif log == './':
                continue
            else:
                stk += 1

        return stk 