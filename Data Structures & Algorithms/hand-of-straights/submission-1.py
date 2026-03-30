class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()

        currSize = 1
        last = hand.pop(0)
        ptr = 0

        while hand and ptr < len(hand):
            if currSize == groupSize:
                currSize = 0
                ptr = 0
                last = -1
                continue
            if hand[ptr] == last + 1 or last == -1:
                last = hand.pop(ptr)
                currSize += 1
                continue
            ptr += 1

        return currSize == groupSize  and len(hand) == 0