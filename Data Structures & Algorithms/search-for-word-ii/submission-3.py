class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # put all words into a Trie
        wordTrie = Trie()
        for w in words:
            wordTrie.insert(w)

        resultList = set()

        # use bfs to search for words that start with the letter in the grid
        height = len(board)
        width = len(board[0])

        def dfs(pos, ptr: Node, path: str):
            y, x = pos

            curr = board[y][x]
            if curr not in ptr.children:
                return

            nxt = ptr.children[curr]
            nxtPath = path + curr

            if nxt.terminal:
                resultList.add(nxtPath)

            board[y][x] = "#"

            diff = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dy, dx in diff:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < height and 0 <= nx < width and board[ny][nx] != "#":
                    dfs((ny, nx), nxt, nxtPath)

            board[y][x] = curr

        for y in range(height):
            for x in range(width):
                dfs((y, x), wordTrie.root, "")

        return [r for r in resultList]


class Node:
    def __init__(self):
        self.children = {}
        self.terminal = False


class Trie:

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