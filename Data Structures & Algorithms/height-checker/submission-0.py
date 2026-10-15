class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        nh = heights[:]
        nh.sort()
        total = 0

        for i in range(len(heights)):
            if heights[i] != nh[i]:
                total += 1
        return total 