class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boatCount = 0
        people.sort()

        left, right = 0, len(people) - 1
        while left < right:
            if people[left] + people[right] > limit:
                people[right] = -1
                right -= 1

                boatCount += 1
                continue
            if people[left] + people[right] <= limit:
                people[left] = -1
                people[right] = -1

                left += 1
                right -= 1
                boatCount += 1
        if left == right and people[left] != -1:
            boatCount += 1
        return boatCount