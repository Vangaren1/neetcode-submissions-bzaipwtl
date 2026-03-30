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

class Solution {
private:
    vector<vector<int>> results;

public:
    vector<vector<int>> levelOrder(TreeNode *root)
    {
        vector<vector<int>> results;

        if (!root)
        {
            return results;
        }

        queue<pair<TreeNode *, int>> nodeQ;

        nodeQ.push({root, 0});

        while (!nodeQ.empty())
        {
            pair<TreeNode *, int> tmp = nodeQ.front();
            nodeQ.pop();

            if (tmp.second + 1 > results.size())
            {
                results.push_back({tmp.first->val});
            }
            else
            {
                results[tmp.second].push_back(tmp.first->val);
            }

            if (tmp.first->left)
            {
                nodeQ.push({tmp.first->left, tmp.second + 1});
            }
            if (tmp.first->right)
            {
                nodeQ.push({tmp.first->right, tmp.second + 1});
            }
        }

        return results;
    }
};
