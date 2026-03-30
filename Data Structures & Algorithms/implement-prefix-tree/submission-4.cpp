#include <array>
class PrefixTree
{
private:
    class Node
    {
    public:
        array<Node *, 26> children{};
        bool terminal = false;
    };
    Node *root;

public:
    PrefixTree()
    {
        root = new Node();
    }

    void insert(string word)
    {
        Node *ptr = root;
        for (char ch : word)
        {
            if (ptr->children[ch - 'a'] == nullptr)
            {
                ptr->children[ch - 'a'] = new Node();
            }
            ptr = ptr->children[ch - 'a'];
        }
        ptr->terminal = true;
    }

    bool search(string word)
    {
        Node *ptr = root;
        for (char ch : word)
        {
            if (ptr->children[ch - 'a'] == nullptr)
            {
                return false;
            }
            ptr = ptr->children[ch - 'a'];
        }
        return ptr->terminal;
    }

    bool startsWith(string prefix)
    {
        Node *ptr = root;
        for (char ch : prefix)
        {
            if (ptr->children[ch - 'a'] == nullptr)
            {
                return false;
            }
            ptr = ptr->children[ch - 'a'];
        }
        return true;
    }
};
