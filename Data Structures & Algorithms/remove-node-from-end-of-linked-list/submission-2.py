# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the length
        count = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            count += 1

        if count == n:
            return head.next
        # go to the node before the nth node
        ptr = ListNode()
        ptr.next = head
        for i in range(count - n):
            ptr = ptr.next

        if ptr and ptr.next:
            ptr.next = ptr.next.next

        return head