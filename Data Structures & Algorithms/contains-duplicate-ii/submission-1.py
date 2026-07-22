class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        curr = {}

        for index, val in enumerate(nums):
            if val in curr:
                if abs(index - curr[val]) <= k:
                    return True
            curr[val] = index

        return False