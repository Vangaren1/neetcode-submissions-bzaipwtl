class Node
{
public:
    unordered_map<char, Node *> children;
    bool terminal = false;
};

class PrefixTree
{
private:
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
            if (ptr->children.count(ch) == 0)
            {
                ptr->children[ch] = new Node();
            }
            ptr = ptr->children[ch];
        }
        ptr->terminal = true;
    }

    bool search(string word)
    {
        Node *ptr = root;
        for(char ch : word){
            if(ptr->children.count(ch)==0){
                return false;
            }
            ptr = ptr->children[ch];
        }
        return ptr->terminal;
    }

    bool startsWith(string prefix)
    {
        Node *ptr = root;
        for(char ch : prefix){
            if(ptr->children.count(ch)==0){
                return false;
            }
            ptr = ptr->children[ch];
        }
        return true;
    }
};
