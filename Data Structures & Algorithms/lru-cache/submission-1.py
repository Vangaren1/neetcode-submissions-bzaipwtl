class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache.get(key)

    def put(self, key: int, value: int) -> None:
        if self.cap == len(self.cache) and key not in self.cache:
            self.cache.popitem(last=False)
        self.cache[key] = value
        self.cache.move_to_end(key)