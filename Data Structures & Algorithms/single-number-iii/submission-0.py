class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n == 2:
            return nums

        xorTotal = 0
        for num in nums:
            xorTotal ^= num

        print(bin(xorTotal))

        # find the ith bit that is 0
        i = 0

        while i < 32:
            if xorTotal & (1 << i):
                break
            i += 1
        mask = 1 << i

        xor1 = 0
        xor0 = 0

        for num in nums:
            if num & mask:
                xor0 ^= num
            else:
                xor1 ^= num

        return [xor1, xor0]