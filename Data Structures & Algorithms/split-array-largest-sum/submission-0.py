class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = left + (right - left) // 2
            peices = 1
            curr = 0
            for num in nums:
                if num + curr > mid:
                    peices += 1
                    curr = num
                else:
                    curr += num

            if peices <= k:
                right = mid - 1
            else:
                left = mid + 1
        return left