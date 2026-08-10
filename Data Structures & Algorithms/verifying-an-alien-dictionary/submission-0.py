class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        alien = {ch: index for index, ch in enumerate(order)}

        for index in range(len(words) - 1):
            first = words[index]
            second = words[index + 1]

            ptr = 0
            length = min(len(first), len(second))
            diff = False
            for idx in range(length):

                if alien[first[idx]] > alien[second[idx]] and not diff:
                    return False
                if first[idx] != second[idx]:
                    diff = True
            if not diff and len(second) < len(first):
                return False

        return True