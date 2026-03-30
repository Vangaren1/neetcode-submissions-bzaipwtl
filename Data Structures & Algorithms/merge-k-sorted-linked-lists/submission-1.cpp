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
ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        int m{0}, n = lists.size();

        if( n == 0){
            return nullptr;
        }
        if(n == 1){
            return lists[0];
        }

        while (lists.size() > 1)
        {
            n = lists.size() - 1;
            
            ListNode *a = lists[n];
            ListNode *b = lists[n-1];

            lists[n-1] = mergeTwoLists(a,b);
            lists.pop_back();
        }
        return lists[0];
    }

    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        ListNode *head = new ListNode(0);
        ListNode *ptr = head;

        while (list1 != nullptr && list2 != nullptr)
        {
            if (list1->val < list2->val)
            {
                ptr->next = list1;
                list1 = list1->next;
            }
            else
            {
                ptr->next = list2;
                list2 = list2->next;
            }
            ptr = ptr->next;
        }

        if (list1 != nullptr)
        {
            ptr->next = list1;
        }
        else
        {
            ptr->next = list2;
        }

        return head->next;
    }
};
