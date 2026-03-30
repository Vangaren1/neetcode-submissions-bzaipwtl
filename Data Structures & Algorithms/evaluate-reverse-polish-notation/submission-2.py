class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        func = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: y - x,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(y / x),
        }

        stk = []

        for tok in tokens:
            if tok.isnumeric() or tok[0] == "-" and len(tok) > 1:
                stk.append(tok)
            else:
                x = stk.pop()
                y = stk.pop()
                stk.append(func[tok](int(x), int(y)))

        return int(stk.pop())