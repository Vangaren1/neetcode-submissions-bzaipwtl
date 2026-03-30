/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node *, Node *> oldToNew;

        Node *ptr = head, *tmp;
        while (ptr)
        {
            tmp = new Node(ptr->val);
            oldToNew[ptr] = tmp;
            ptr = ptr->next;
        }

        ptr = head;

        while(ptr){
            oldToNew[ptr]->next = oldToNew[ptr->next];
            oldToNew[ptr]->random = oldToNew[ptr->random];
            ptr = ptr->next;
        }
        return oldToNew[head];
    }
};
