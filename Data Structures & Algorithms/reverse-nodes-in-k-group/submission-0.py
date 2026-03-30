# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dq = deque([])
        newHead = ListNode()
        ptr = head
        newHead.next = ptr
        front = newHead
        while ptr:
            # put k items in the deque and mark the end
            tmp = ptr

            for _ in range(k):
                if tmp:
                    dq.appendleft(tmp)
                    tmp = tmp.next
            # if the dq has enough to flip, mark the start of the next batch and empty the dq
            if len(dq) == k:
                nxt = tmp
                while dq:
                    n = dq.pop()
                    n.next = nxt
                    nxt = n
                # need to point the front to nxt
                front.next = nxt
                # need to update the front to the next front
                for _ in range(k):
                    front = front.next
            ptr = tmp

        return newHead.next