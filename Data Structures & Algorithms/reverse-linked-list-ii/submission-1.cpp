/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
                ListNode *front = new ListNode(0);
        front->next = head;

        ListNode *first = front;
        for (int i = 0; i < left - 1; i++)
        {
            first = first->next;
        }

        ListNode *second = first;
        for (int j = 0; j < right - left + 1; j++)
        {
            second = second->next;
        }

        ListNode *end = second->next;
        ListNode *ptr1 = first->next;
        ListNode *ptr2 = ptr1->next;
        ListNode *tmp;
        ptr1->next = end;

        while (ptr2 != end)
        {
            tmp = ptr2->next;
            ptr2->next = ptr1;
            ptr1 = ptr2;
            ptr2 = tmp;
        }
        first->next = ptr1;
        return front->next;
    }
};