class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        def hop(val):
            while nums[val - 1] != val:
                curr = nums[val - 1]
                nums[val - 1] = val
                if curr <= 0 or curr > n + 1:
                    break
                val = curr

        for index in range(len(nums)):
            if nums[index] <= 0 or nums[index] > n :
                nums[index] = 0
                continue
            hop(nums[index])

        for index in range(len(nums)):
            if nums[index] != index + 1:
                return index + 1
        return n+1