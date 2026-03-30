class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def toEat(piles, rate):
            total = 0
            for stack in piles:
                eaten = math.ceil(stack / rate)
                total += eaten
            return total

        biggest = max(piles)

        seen = {}

        def binSearch(ceiling):
            left = 1
            right = ceiling

            while left <= right:
                mid = (left + right) // 2
                check = toEat(piles, mid)
                seen[mid] = check
                if check > h:
                    left = mid + 1
                else:
                    right = mid - 1
            return mid

        k = binSearch(biggest)
        ran = [k]
        if k > 1 and k - 1 not in seen:
            seen[k - 1] = toEat(piles, k - 1)
            ran.append(k - 1)

        if seen[k] > h or k == 1:
            if k + 1 not in seen:
                seen[k + 1] = toEat(piles, k + 1)
            ran.append(k + 1)

        r = [i for i in ran if seen[i] <= h]
        return min(r)