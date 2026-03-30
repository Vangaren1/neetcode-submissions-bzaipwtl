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
    void reorderList(ListNode *head)
    {
        ListNode *slow = head, *fast = head;

        while (fast->next != nullptr && fast->next->next != nullptr)
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode *second = slow->next;
        second = reverseList(second);
        slow->next = nullptr;

        head = mergeTwoLists(head, second);
    }

    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        ListNode *head = new ListNode(0);
        ListNode *ptr = head;

        int counter = 0;
        while (list1 != nullptr && list2 != nullptr)
        {
            
            if (counter % 2 == 0)
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
            counter++;
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
    ListNode *reverseList(ListNode *head)
    {

        ListNode *curr = head;
        ListNode *prev = nullptr;
        ListNode *next = nullptr;

        while (curr != nullptr)
        {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

};