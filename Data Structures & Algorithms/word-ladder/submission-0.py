import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return 0
        if len(beginWord) != len(endWord):
            return 0
        if beginWord == endWord:
            return 0
        
        queue = [(beginWord, 1)]
        letters = string.ascii_lowercase
        
        while queue:
            
            curr, step = queue.pop(0)
            
            for index in range(len(curr)):
                for l in letters:
                    tmp = curr[:index] + l + curr[index + 1:]
                    if tmp in wordSet:
                        if tmp == endWord:
                            return step + 1
                        queue.append((tmp, step+1))
                        wordSet.remove(tmp)
        return 0