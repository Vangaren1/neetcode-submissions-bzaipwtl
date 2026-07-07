class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m -= 1
        n -= 1
        finish1 = False
        for ptr1 in range(len(nums1) - 1, -1, -1):
            if m >= 0 and n >= 0:
                if nums1[m] >= nums2[n]:
                    nums1[ptr1] = nums1[m]
                    m -= 1
                else:
                    nums1[ptr1] = nums2[n]
                    n -= 1
            else:
                if n >= 0:
                    nums1[ptr1] = nums2[n]
                    n -= 1