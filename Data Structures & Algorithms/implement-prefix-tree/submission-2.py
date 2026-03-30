class Node:
    def __init__(self):
        self.children = {}
        self.terminal = False


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        ptr = self.root
        for w in word:
            if w not in ptr.children:
                ptr.children[w] = Node()
            ptr = ptr.children[w]
        ptr.terminal = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for w in word:
            if w not in ptr.children:
                return False
            ptr = ptr.children[w]
        return ptr.terminal

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for w in prefix:
            if w not in ptr.children:
                return False
            ptr = ptr.children[w]
        return ptr != None