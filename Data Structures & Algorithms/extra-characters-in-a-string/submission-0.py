class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        pft = PrefixTree()
        for word in dictionary:
            pft.insert(word)

        n = len(s)

        dp = [0 for _ in range(n + 1)]

        for index in range(n - 1, -1, -1):
            dp[index] = 1 + dp[index + 1]

            ptr = pft.root

            for j in range(index, n):
                ch = s[j]

                if ch not in ptr.children:
                    break
                ptr = ptr.children[ch]

                if ptr.terminal:
                    dp[index] = min(dp[index], dp[j + 1])

        return dp[0]


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

