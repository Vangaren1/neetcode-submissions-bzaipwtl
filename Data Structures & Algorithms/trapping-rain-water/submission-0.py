class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        for index in range(1, len(height)):
            maxLeft[index] = max(height[index - 1], maxLeft[index - 1])
        for index in range(len(height) - 2, -1, -1):
            maxRight[index] = max(height[index + 1], maxRight[index + 1])

        total = 0

        for index in range(len(height)):
            maxH = min(maxLeft[index], maxRight[index])
            val = maxH - height[index]
            if val > 0:
                total += val

        return total