class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = defaultdict(int)
        for n in nums: 
            count[n]+=1
        k = len(nums) - count[val]
        count[val] = 0
        ptr = 0 
        for key, val in count.items():
            for i in range(val):
                nums[ptr + i] = key
            ptr += val
        return k