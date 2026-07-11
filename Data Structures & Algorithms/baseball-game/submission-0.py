class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for op in operations:
            if op not in ("+", "C", "D"):
                stk.append(int(op))
            elif op == "+":
                stk.append(stk[-1] + stk[-2])
            elif op == "C":
                stk.pop()
            elif op == "D":
                stk.append(2 * stk[-1])
        return sum(stk)