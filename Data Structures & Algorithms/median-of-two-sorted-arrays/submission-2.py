class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        larger, smaller = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(larger) < len(smaller):
            larger, smaller = smaller, larger

        left, right = 0, len(smaller) - 1
        while True:
            midSmall = (left + right) // 2
            midLarge = half - midSmall - 2

            leftSmall = smaller[midSmall] if midSmall >= 0 else float("-inf")
            rightSmall = (
                smaller[midSmall + 1] if (midSmall + 1) < len(smaller) else float("inf")
            )
            leftLarge = larger[midLarge] if midLarge >= 0 else float("-inf")
            rightLarge = (
                larger[midLarge + 1] if (midLarge + 1) < len(larger) else float("inf")
            )

            if leftSmall <= rightLarge and leftLarge <= rightSmall:
                # partitioning is correct
                if total % 2 == 1:
                    return min(rightLarge, rightSmall)

                m = max(leftLarge, leftSmall) + min(rightLarge, rightSmall)
                return m / 2
            elif leftSmall > rightLarge:
                right = midSmall - 1
            else:
                left = midSmall + 1