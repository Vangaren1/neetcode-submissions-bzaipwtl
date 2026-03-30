class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        def dfs(index, goal):
            if index == len(nums) or goal < 0:
                return False
            curr = nums[index]
            if curr == goal:
                return True
            include = dfs(index + 1, goal - curr)
            exclude = dfs(index + 1, goal)
            return include or exclude

        return dfs(0, total // 2)