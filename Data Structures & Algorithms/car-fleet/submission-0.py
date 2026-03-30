class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def colide(a, b):
            # returns true if A arrives before B or at the same time
            arriveA = (target - a[0]) / a[1]
            arriveB = (target - b[0]) / b[1]
            return arriveA <= arriveB

        posM = []

        for index, pos in enumerate(position):
            s = speed[index]
            posM.append((pos, s))

        posM.sort(key=lambda x: x[0], reverse=True)

        carStack = []
        for car in posM:
            carStack.append(car)
            if len(carStack) > 1 and colide(carStack[-1], carStack[-2]):
                carStack.pop()

        return len(carStack)