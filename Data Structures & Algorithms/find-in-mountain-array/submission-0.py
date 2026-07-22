class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        left, right = 0, mountainArr.length() - 1

        seen = {left: mountainArr.get(left), right: mountainArr.get(right)}

        if seen[left] == target:
            return left

        # find the peak, i.e. where seen[index] > seen[index+1]

        while left < right:

            mid = left + (right - left) // 2
            if mid not in seen:
                seen[mid] = mountainArr.get(mid)
            if mid + 1 not in seen:
                seen[mid + 1] = mountainArr.get(mid + 1)

            if seen[mid] < seen[mid + 1]:
                # still in left half
                left = mid + 1
            else:
                right = mid - 1

        # left = peak value
        # check left side now
        peak = left
        right = left
        left = 0
        while left <= right:
            mid = left + (right - left) // 2
            if mid not in seen:
                seen[mid] = mountainArr.get(mid)

            if seen[mid] == target:
                return mid
            if seen[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # if not in left half, then in right half
        left = peak + 1
        right = mountainArr.length() - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid not in seen:
                seen[mid] = mountainArr.get(mid)
            if seen[mid] == target:
                return mid
            if seen[mid] < target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
