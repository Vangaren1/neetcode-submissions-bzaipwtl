class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyVal = {}
        self.count = defaultdict(int)
        self.freq = defaultdict(list)
        self.least = 0

    def get(self, key: int) -> int:
        if key not in self.keyVal:
            return -1

        currCount = self.count[key]
        self.freq[currCount].remove(key)
        if currCount == self.least and len(self.freq[currCount]) == 0:
            self.least += 1
        self.count[key] += 1
        self.freq[currCount + 1].append(key)
        return self.keyVal.get(key)

    def put(self, key: int, value: int) -> None:
        def addNew(k, v):
            self.keyVal[k] = v
            self.count[k] = 0
            self.freq[0].append(k)
            self.least = 0
            return

        # if it's already in, update the frequency and value
        if key in self.keyVal:
            self.get(key)
            self.keyVal[key] = value
            return

        # if its empty or less than capacity, just add it
        if len(self.keyVal) < self.capacity:
            addNew(key, value)
            return

        # if its a new value, evict the least frequently used and then add it

        leastKey = self.freq[self.least].pop(0)
        self.keyVal.pop(leastKey)
        self.count.pop(leastKey)
        addNew(key, value)