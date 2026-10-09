class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        allNum = set([ i for i in range(1,n+1)])
        diff = allNum - set(nums)
        return [ i for i in diff]