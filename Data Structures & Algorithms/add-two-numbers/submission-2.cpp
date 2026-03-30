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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = new ListNode(0);
        ListNode *ptr = head;
        int carry{0}, tmp{0}, val1{0}, val2{0};

        while (l1 || l2 || carry)
        {
            val1 = l1 ? l1->val : 0;
            val2 = l2 ? l2->val : 0;
            tmp = val1 + val2 + carry;
            ptr->next = new ListNode(tmp % 10);
            carry = tmp / 10;
            if (l1)
                l1 = l1->next;
            if (l2)
                l2 = l2->next;
            ptr = ptr->next;
        }

        return head->next;
    }
};
