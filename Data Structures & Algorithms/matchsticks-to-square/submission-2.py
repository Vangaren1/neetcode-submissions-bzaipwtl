

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total // 4

        sides = [0, 0, 0, 0]

        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False

        def backtrack(index):
            if index == len(matchsticks):
                return all(sides[i] == target for i in range(len(sides)))

            for s in range(4):
                if sides[s] + matchsticks[index] <= target:
                    sides[s] += matchsticks[index]

                    if backtrack(index + 1):
                        return True

                    sides[s] -= matchsticks[index]

            return False

        return backtrack(0)