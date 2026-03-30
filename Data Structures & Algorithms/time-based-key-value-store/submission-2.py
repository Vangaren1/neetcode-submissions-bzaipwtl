class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        array = self.store.get(key)
        return self.binSearch(array, timestamp)

    def binSearch(self, array: list, timestamp: int):
        if array == None or len(array) == 0:
            return ""

        if timestamp < array[0][1]:
            return ""

        if timestamp < array[0][1]:
            return ""

        left = 0
        right = len(array) - 1
        result = ""
        while left <= right:
            mid = (left + right) // 2
            curr = array[mid][1]
            if timestamp == curr:
                return array[mid][0]
            if timestamp > curr:
                result = array[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return result