# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newHead = ListNode()

        ptr = newHead

        while lists:
            listPtr = None
            index = -1
            for idx, lst in enumerate(lists):
                if lst is None:
                    continue
                # grab the list with the lowest value
                if listPtr is None or lst.val < listPtr.val:
                    index = idx
                    listPtr = lst
            # point the head towards that
            ptr.next = listPtr
            # increment the listPtr to the next value (or none)
            lists[index] = lists[index].next
            # if its the last, remove it from the list
            if lists[index] == None:
                lists.pop(index)
                index = -1
            ptr = ptr.next

        return newHead.next