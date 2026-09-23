class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        # can't have less than 1, and can't have 2 because then there wouldn't be a unique number
        if n == 1:
            return nums[0]

        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2

            # consider the extreme ends of the arrays
            if mid == n - 1 and nums[mid] != nums[mid - 1]:
                return nums[mid]
            elif mid == 0 and nums[mid] != nums[mid + 1]:
                return nums[0]

            # check if mid is the single number
            if nums[mid - 1] != nums[mid] != nums[mid + 1]:
                return nums[mid]

            # before the single number, the pairs are even, odd.
            # after the single number, the pairs are odd, even
            if nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    left = mid + 1
                else:
                    right = mid - 1
                continue
            else:
                if mid % 2 == 0:
                    right = mid - 1
                else:
                    left = mid + 1