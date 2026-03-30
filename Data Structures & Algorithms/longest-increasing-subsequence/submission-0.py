class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []

        for num in nums:
            check = [n for n in seq if n[-1] < num]
            if len(check) == 0:
                seq.append([num])
                continue
            for c in check:
                seq.append(c.copy())
                c.append(num)

        return max([len(s) for s in seq])