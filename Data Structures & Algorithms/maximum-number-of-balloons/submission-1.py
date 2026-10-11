class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        maximum = float('inf')

        for ch in "ban":
            maximum = min(maximum, c[ch])
        for ch in "lo":
            maximum = min(maximum, c[ch]//2)
        return maximum