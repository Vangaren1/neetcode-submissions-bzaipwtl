class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.groups = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        count = self.freq[val]

        self.groups[count].append(val)
        self.maxFreq = max(self.maxFreq, count)

    def pop(self) -> int:
        val = self.groups[self.maxFreq].pop()
        self.freq[val] -= 1
        if not self.groups[self.maxFreq]:
            self.maxFreq -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()