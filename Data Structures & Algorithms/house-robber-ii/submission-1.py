class Solution:
    def rob(self, nums: List[int]) -> int:

        first = nums[0] + self.rob1(nums[2:-1])
        second = self.rob1(nums[1:])
        return max(first, second)

    def rob1(self, nums: List[int]) -> int:

        rob1, rob2 = 0, 0

        for n in nums:
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2