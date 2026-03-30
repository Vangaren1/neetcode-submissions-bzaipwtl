class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nDict = {}
        for index, val in enumerate(nums):
            nDict[target-val] = index
        for index in range(len(nums)):
            if nums[index] in nDict and nDict[nums[index]] != index:
                return [index, nDict[nums[index]]]
            