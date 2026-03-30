# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()

        ptr = newHead
        while list1 and list2:
            if list1.val <= list2.val:
                tmp = list1
                list1 = list1.next
            else:
                tmp = list2
                list2 = list2.next
            tmp.next = None
            ptr.next = tmp
            ptr = ptr.next

        if list1:
            ptr.next = list1

        if list2:
            ptr.next = list2

        return newHead.next