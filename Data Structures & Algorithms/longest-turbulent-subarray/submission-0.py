class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1

        compare = []

        for index in range(1, n):
            if arr[index] > arr[index - 1]:
                compare.append(1)
            elif arr[index] < arr[index - 1]:
                compare.append(-1)
            else:
                compare.append(0)

        best = 1
        count = 1

        for index in range(len(compare)):
            if compare[index] == 0:
                count = 1
            elif index > 0 and compare[index] == -compare[index - 1]:
                count += 1
            else:
                count = 2

            best = max(best, count)
        return best
