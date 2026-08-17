class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = [0, 0, 0]

        for bill in bills:
            if bill == 5:
                cash[0] += 1
                continue
            elif bill == 10:
                if cash[0] == 0:
                    return False
                cash[0] -= 1
                cash[1] += 1
            elif bill == 20:
                if cash[1]:
                    if cash[0] == 0:
                        return False
                    cash[0] -= 1
                    cash[1] -= 1
                    cash[2] += 1
                    continue
                elif cash[0] < 3 and cash[1] == 0:
                    return False
                cash[0] -= 3
                cash[2] += 1

        return True