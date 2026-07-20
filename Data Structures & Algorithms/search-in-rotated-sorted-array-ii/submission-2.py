class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        s = set(nums)
        return target in s