class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        dp = [0 for _ in range(len(arr))]
        for index in range(len(arr)-2, -1, -1):
            dp[index] = max(arr[index+1] , dp[index+1])
        

\
        dp[-1]=-1
        return dp


