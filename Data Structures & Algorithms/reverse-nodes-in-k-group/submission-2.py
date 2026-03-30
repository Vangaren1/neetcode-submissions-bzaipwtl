# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy
        
        count = 0
        for _ in range(k):
            ptr = ptr.next
            if ptr == None:
                break
            count += 1
        if count != k:
            return head  

        tmp1, tmp2 = ptr.next, dummy.next 
        
        ptr.next = None
        dummy.next = self.reverseList(dummy.next)
        tmp2.next = self.reverseKGroup(tmp1, k)
        
        return dummy.next
        
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        ptr1 = head
        ptr2 = ptr1.next
        ptr1.next = None

        while ptr2:
            tmp = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = tmp

        return ptr1