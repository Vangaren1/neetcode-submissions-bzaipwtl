class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        mArea = 0
        mLeft, mRight = 0, 0

        while left < right:
            mLeft = max(mLeft, heights[left])
            mRight = max(mRight, heights[right])
            volume = min(mLeft, mRight) * (right - left)
            mArea = max(mArea, volume)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return mArea