class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        dp = [0]

        for index in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                dp.append(1)
            elif nums[index] < nums[index - 1]:
                dp.append(-1)
            else:
                dp.append(0)

        best = 1
        ptr = 1
        currInc = 1
        currDec = 1
        while ptr < len(nums):
            if dp[ptr] == 1:
                currInc += 1
                currDec = 1
            elif dp[ptr] == -1:
                currInc = 1
                currDec += 1
            else:
                currInc = 1
                currDec = 1

            best = max(best, currInc, currDec)
            ptr += 1

        return best
            