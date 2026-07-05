class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for index in range(len(s)//2):
            s[index], s[-1-index] = s[-1-index], s[index]