# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ptr = head

        while ptr and ptr.next:
            g = math.gcd(ptr.val, ptr.next.val)
            tmp = ptr.next
            ptr.next = ListNode(g, next=tmp)
            ptr = ptr.next.next

        return head