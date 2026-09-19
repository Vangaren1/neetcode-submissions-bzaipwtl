class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        second = { val:index for index, val in enumerate(nums2)}
        results = []

        for num in nums1:
            index = second[num]
            ptr = index + 1
            while ptr < n and nums2[ptr] < num:
                ptr += 1
            if ptr == n:
                results.append(-1)
            else:
                results.append(nums2[ptr])
        return results