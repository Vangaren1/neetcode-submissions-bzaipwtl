import random 

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def partition(low, high):
            pivot_index = random.randint(low, high)
            swap(pivot_index, high)
            pivot = nums[high]
            i = low - 1
            for j in range(low, high):
                if nums[j] < pivot:
                    i += 1
                    swap(i, j)
            swap(i + 1, high)
            return i + 1

        def quick(low, high):
            if low < high:
                pivot = partition(low, high)
                quick(low, pivot - 1)
                quick(pivot + 1, high)

        quick(0, len(nums) - 1)
        return nums