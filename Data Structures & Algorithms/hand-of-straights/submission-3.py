class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        
        for card in sorted(count):
            while count[card] >0:
                for x in range(card, card + groupSize):
                    if count[x] == 0:
                        return False
                    count[x] -=1 
        return True