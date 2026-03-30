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

        if (n == 0)
        {
            return nullptr;
        }
        if (n == 1)
        {
            return lists[0];
        }

        return mergeRange(lists, 0, n-1);
    }

    ListNode *mergeRange(vector<ListNode *> &lists, int left, int right){
        if( left == right){
            return lists[left];
        }

        int mid = (left + right)/2 ;

        ListNode *leftList = mergeRange(lists, left, mid);
        ListNode *rightList = mergeRange(lists, mid+1, right);
        
        return mergeTwoLists(leftList, rightList);
    }


    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        ListNode head(0);
        ListNode *ptr = &head;

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

        return head.next;
    }
};
