class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        curr = set()
        size = 0
        # create the sliding window
        for index in range(len(nums)):

            if nums[index] in curr:
                return True
            curr.add(nums[index])
            if size == k:
                curr.remove(nums[index - k])
            else:
                size += 1

        return False