class PrefixTree:

    class trieNode:
        def __init__(self):
            self.children = [
                None,
            ] * 26
            self.end = False

    def __init__(self):
        self.start = [
            None,
        ] * 26

    def insert(self, word: str) -> None:
        ptr = self.start
        for index, w in enumerate(word):
            idx = ord(w) - ord("a")
            if ptr[idx] == None:
                ptr[idx] = self.trieNode()
            if index == len(word) - 1:
                ptr[idx].end = True
            ptr = ptr[idx].children

    def search(self, word: str) -> bool:
        ptr = self.start
        for index, w in enumerate(word):
            idx = ord(w) - ord("a")
            if not ptr[idx]:
                return False
            if index == len(word) - 1:
                return ptr[idx].end
            ptr = ptr[idx].children
        return False

    def startsWith(self, prefix: str) -> bool:
        ptr = self.start
        for index, w in enumerate(prefix):
            idx = ord(w) - ord("a")
            if not ptr[idx]:
                return False
            if index == len(prefix) - 1:
                return ptr[idx] != None
            ptr = ptr[idx].children
        return False