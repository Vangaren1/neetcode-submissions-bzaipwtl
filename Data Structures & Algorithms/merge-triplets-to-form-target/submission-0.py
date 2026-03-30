class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = False, False, False
        for first, second, third in triplets:
            if first > target[0] or second > target[1] or third > target[2]:
                continue
            if first == target[0]:
                a = True
            if second == target[1]:
                b = True
            if third == target[2]:
                c = True
            if a and b and c:
                break

        return a and b and c