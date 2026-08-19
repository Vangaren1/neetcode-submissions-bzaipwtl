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
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
                ListNode *ptr = head;
        while (ptr && ptr->next)
        {
            ListNode *tmp = ptr->next;
            ptr->next = new ListNode(gcd(ptr->val, ptr->next->val), tmp);
            ptr = ptr->next->next;
        }
        return head;
    }
};