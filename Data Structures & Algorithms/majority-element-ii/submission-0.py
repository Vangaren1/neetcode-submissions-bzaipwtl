class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        n = len(nums)
        return [key for key, val in count.items() if val * 3 > n]