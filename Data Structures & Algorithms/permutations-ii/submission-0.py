class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = set()
        n = len(nums)

        if n == 1:
            return [nums]

        for index in range(n):

            arr = nums.copy()
            tmp = arr.pop(index)

            permutations = self.permuteUnique(arr)

            for perm in permutations:
                t = [tmp] + perm
                results.add(tuple(t))

        return [[i for i in perm] for perm in results]