class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        n = len(nums)

        used = [False for _ in range(n)]

        def backtrack(currSum, segs, start):
            if segs == k:
                return currSum == 0 and all(used)
            if currSum == target:
                return backtrack(0, segs + 1, 0)

            for index in range(start, n):
                if used[index]:
                    continue
                if nums[index] + currSum > target:
                    continue
                used[index] = True
                if backtrack(currSum + nums[index], segs, index + 1):
                    return True
                used[index] = False

            return False

        return backtrack(0, 0, 0)