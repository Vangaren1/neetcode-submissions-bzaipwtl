class Solution:
    class sortedList:
        def __init__(self):
            self.hq = []

        def size(self):
            return len(self.hq)

        def insert(self, val):
            if self.size() == 0:
                self.hq.append(val)
            else:
                insertPoint = self.find(val)
                self.hq.insert(insertPoint, val)

        def find(self, val):
            lo, hi = 0, self.size()
            while lo < hi:
                mid = (lo + hi) // 2
                if self.hq[mid] < val:
                    lo = mid + 1
                else:
                    hi = mid

            return lo

        def remove(self, val):
            index = self.find(val)
            if index < self.size() and self.hq[index] == val:
                self.hq.pop(index)
                return True
            return False

        def getMax(self):
            if self.size() > 0:
                return self.hq[-1]
            return None

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []

        hp = self.sortedList()

        for index in range(k):
            n = nums[index]
            hp.insert(n)

        results.append(hp.getMax())

        for index in range(len(nums) - k):
            # remove the front value
            hp.remove(nums[index])
            if (index + k) < len(nums):
                hp.insert(nums[index + k])
                results.append(hp.getMax())

        return results