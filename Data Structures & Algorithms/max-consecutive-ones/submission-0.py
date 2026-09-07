class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxSeen = 0 

        count = 0 
        for num in nums:
            if num == 1:
                count += 1
                maxSeen = max(maxSeen, count)
            else:
                count = 0
        return maxSeen