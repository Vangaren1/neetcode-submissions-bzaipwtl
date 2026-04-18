/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
Node *cloneGraph(Node *node)
    {
        unordered_map<Node *, Node *> nodemap;

        return dfs(node, nodemap);
    }

    Node *dfs(Node *node, unordered_map<Node *, Node *> &nmap)
    {
        if (node == nullptr)
        {
            return nullptr;
        }
        if (nmap.count(node) > 0)
        {
            return nmap[node];
        }
        nmap[node] = new Node(node->val);
        for (Node *tmp : node->neighbors)
        {
            Node *neighbor = dfs(tmp, nmap);
            nmap[node]->neighbors.push_back(neighbor);
        }
        

        return nmap[node];
    }
};
