class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opened, closed = 0, 0

        stack = []
        res = []

        def recParen(open, closed):
            if open == closed == n:
                res.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                recParen(open + 1, closed)
                stack.pop()

            if closed < open:
                stack.append(")")
                recParen(open, closed + 1)
                stack.pop()

        recParen(0, 0)
        return res