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
        int carry{0}, tmp{0};

        while (l1 && l2)
        {
            tmp = l1->val + l2->val + carry;
            ptr->next = new ListNode(tmp % 10);
            carry = (tmp > 9) ? 1 : 0;
            l1 = l1->next;
            l2 = l2->next;
            ptr = ptr->next;
        }

        ListNode *remaining = ( l1 != nullptr) ? l1 : l2;

        while(remaining){
            tmp = remaining->val + carry;
            ptr->next = new ListNode(tmp % 10);
            carry = (tmp > 9) ? 1 : 0;
            ptr = ptr->next;
            remaining = remaining->next;
        }

        if(carry == 1){
            ptr->next = new ListNode(1);
        }

        return head->next;
    }
};
