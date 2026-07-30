class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyVal = {}
        self.count = {}
        self.freq = defaultdict(OrderedDict)
        self.least = 0

    def _increaseFreq(self, key):
        curr = self.count.get(key)
        del self.freq[curr][key]

        if curr == self.least and not self.freq[curr]:
            self.least += 1
        self.count[key] = curr + 1
        self.freq[curr + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.keyVal:
            return -1

        self._increaseFreq(key)
        return self.keyVal.get(key)

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        def addNew(k, v):
            self.keyVal[k] = v
            self.count[k] = 0
            self.freq[0][k] = None
            self.least = 0
            return

        # if it's already in, update the frequency and value
        if key in self.keyVal:
            self.get(key)
            self.keyVal[key] = value
            return

        # if its at capacity, remove least frequently used
        if len(self.keyVal) == self.capacity:
            leastKey, _ = self.freq[self.least].popitem(last=False)
            del self.keyVal[leastKey]
            del self.count[leastKey]

        addNew(key, value)