class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stk = []
        for p in paths:
            if p:
                if p == "..":
                    if stk:
                        stk.pop()
                elif p == ".":
                    continue
                else:
                    stk.append(p)
        return "/" + "/".join(stk)