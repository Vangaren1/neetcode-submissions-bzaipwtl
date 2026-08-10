class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        alien = {ch: index for index, ch in enumerate(order)}

        for index in range(len(words) - 1):
            first = words[index]
            second = words[index + 1]

            match = True
            ptr = 0
            while ptr < len(first) and ptr < len(second) and match:
                if alien[first[ptr]] > alien[second[ptr]]:
                    return False
                if alien[first[ptr]] < alien[second[ptr]]:
                    match = False
                ptr += 1

            if match and len(second) < len(first):
                return False

        return True