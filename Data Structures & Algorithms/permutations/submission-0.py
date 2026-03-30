class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        if len(nums) == 0:
            return [[]]

        if len(nums) == 1:
            return [nums]

        for index in range(len(nums)):

            array = nums.copy()
            curr = array.pop(index)
            sub = self.permute(array)

            for s in sub:
                results.append([curr, *s])

        return results