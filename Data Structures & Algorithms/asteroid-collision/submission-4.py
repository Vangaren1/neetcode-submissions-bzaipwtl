class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def collide(ast):
            stk = []
            for a in ast:
                if not stk or (stk[-1] < 0 and a < 0) or (stk[-1] > 0 and a > 0):
                    stk.append(a)
                elif abs(stk[-1]) == abs(a) and (stk[-1] > 0 and a < 0):
                    stk.pop()
                elif stk[-1] < 0 and a > 0:
                    stk.append(a)
                elif stk[-1] > 0 and a < 0:
                    if abs(stk[-1]) < abs(a):
                        stk.pop()
                        stk.append(a)
                elif stk[-1] < 0 and a > 0:
                    stk.append(a)
            return stk

        stk = collide(asteroids)
        prev = len(stk)
        while stk:
            stk = collide(stk)
            if prev == len(stk):
                break
            prev = len(stk)
        return stk
