class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sumNum = [1]*len(nums)
        self.sumNum[0] = self.nums[0]
        for index in range(1,len(nums)):
            self.sumNum[index] = self.nums[index] + self.sumNum[index-1]
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sumNum[right]
        
        return self.sumNum[right] - self.sumNum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)