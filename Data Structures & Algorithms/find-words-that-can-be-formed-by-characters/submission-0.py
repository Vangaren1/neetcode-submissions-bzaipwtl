class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cc = Counter(chars)
        total = 0

        for word in words:
            wc = Counter(word)
            good = True
            for key, val in wc.items():
                if key not in cc or cc[key] < val:
                    good = False
            if not good:
                continue
            total += len(word)
        return total 