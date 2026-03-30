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

        queue<TreeNode *> nodeQ;

        nodeQ.push(root);

        while (!nodeQ.empty())
        {
            int tmpSize = nodeQ.size();

            vector<int> level;

            for (int i = 0; i < tmpSize; i++)
            {
                TreeNode *tmp = nodeQ.front();
                nodeQ.pop();

                level.push_back(tmp->val);
                if (tmp->left)
                {
                    nodeQ.push(tmp->left);
                }
                if (tmp->right)
                {
                    nodeQ.push(tmp->right);
                }
            }
            results.push_back(level);
        }

        return results;
    }
};
