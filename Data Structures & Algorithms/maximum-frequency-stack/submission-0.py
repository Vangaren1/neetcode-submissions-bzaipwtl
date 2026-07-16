class FreqStack:

    def __init__(self):
        self.hq = []
        self.counter = defaultdict(int)
        self.order = 0

    def push(self, val: int) -> None:
        self.counter[val] += 1
        self.order += 1
        heapq.heappush(self.hq, (-self.counter[val], -self.order, val))

    def pop(self) -> int:
        count, order, val = heapq.heappop(self.hq)
        self.counter[val] -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()