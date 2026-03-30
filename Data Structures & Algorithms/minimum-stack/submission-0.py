

class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        m = None
        if len(self.stk) == 0:
            m = val
        else:
            m = min(self.getMin(), val)
        self.stk.append((val, m))

    def pop(self) -> None:
        return self.stk.pop()[0]

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]