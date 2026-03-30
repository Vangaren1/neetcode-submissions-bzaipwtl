class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        totalGas = 0
        index = 0
        start = 0
        while index < len(gas):
            totalGas += gas[index] - cost[index]

            if totalGas < 0:
                totalGas = 0
                start = index + 1
            index += 1

        return start

