# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        left,right = 0, len(vals)-1

        while left <= right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -=1
        return True
