class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = -1

        c = Counter(arr)
        for key, val in c.items():
            if key == val and key > lucky:
                lucky = key
        return lucky