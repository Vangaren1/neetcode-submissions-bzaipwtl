class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:

            mid = left + (right - left) // 2
            # see if can be done with mid weights in x days
            d = 1
            currWeight = 0
            for weight in weights:
                if currWeight + weight > mid:
                    currWeight = weight
                    d += 1
                else:
                    currWeight += weight
            if d <= days:
                right = mid
            else:
                left = mid + 1
        return left