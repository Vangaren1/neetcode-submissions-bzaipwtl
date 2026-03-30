/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Codec
{
private:
    queue<string> split(string line, char delimiter)
    { // Using str in a string stream
        stringstream ss(line);
        queue<string> res;
        string token;
        while (getline(ss, token, delimiter))
        {
            res.push(token);
        }
        return res;
    }

public:
    // Encodes a tree to a single string.
    string serialize(TreeNode *root)
    {
        if (!root)
        {
            return "";
        }
        queue<TreeNode *> que({root});

        string result = "";

        while (!que.empty())
        {

            TreeNode *tmp = que.front();
            que.pop();

            if (!tmp)
            {
                result += "N,";
                continue;
            }

            result += to_string(tmp->val) + ",";

            que.push(tmp->left);
            que.push(tmp->right);
        }

        int ptr = result.size() - 1;
        while (result[ptr] == ',' || result[ptr] == 'N')
        {
            ptr--;
        }

        return result.substr(0, ptr + 1);
    }

    // Decodes your encoded data to tree.
    TreeNode *deserialize(string data)
    {

        queue<string> nodes = split(data, ',');

        if (nodes.empty())
        {
            return nullptr;
        }

        TreeNode *root = new TreeNode(stoi(nodes.front()));
        nodes.pop();

        queue<TreeNode *> que({root});

        while (!que.empty())
        {
            TreeNode *curr = que.front();
            que.pop();

            if (!nodes.empty())
            {
                string left = nodes.front();
                nodes.pop();
                if (left != "N")
                {
                    curr->left = new TreeNode(stoi(left));
                    que.push(curr->left);
                }
            }
            if (!nodes.empty())
            {
                string right = nodes.front();
                nodes.pop();
                if (right != "N")
                {
                    curr->right = new TreeNode(stoi(right));
                    que.push(curr->right);
                }
            }
        }

        return root;
    }
};