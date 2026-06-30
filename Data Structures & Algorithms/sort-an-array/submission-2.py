class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeS(array):
            if len(array) <= 1:
                return array
            mid = len(array) // 2
            left = mergeS(array[:mid])
            right = mergeS(array[mid:])
            return merge(left, right)

        def merge(left, right):
            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result

        return mergeS(nums)