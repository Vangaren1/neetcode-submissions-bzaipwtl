class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        front = ListNode(0, next=head)

        first = front
        for _ in range(left - 1):
            first = first.next

        second = first
        for _ in range(right - left + 1):
            second = second.next

        end = second.next

        ptr1 = first.next
        ptr2 = ptr1.next
        ptr1.next = end

        while ptr2 != end:
            tmp = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = tmp

        first.next = ptr1
        return front.next