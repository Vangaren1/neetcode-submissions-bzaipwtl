"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeDict = {}
        if head == None:
            return None
        ptr = head
        last = None
        while ptr:
            tmp = Node(ptr.val)
            nodeDict[ptr] = tmp
            ptr = ptr.next

        ptr = head
        while ptr:
            nodeDict[ptr].next = nodeDict.get(ptr.next)
            nodeDict[ptr].random = nodeDict.get(ptr.random)
            ptr = ptr.next
            
        return nodeDict[head]