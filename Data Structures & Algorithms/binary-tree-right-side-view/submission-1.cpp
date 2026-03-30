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
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> results;

        if (!root)
        {
            return results;
        }

        queue<TreeNode *> qNodes({root});

        while (!qNodes.empty())
        {
            int s = qNodes.size();
            int tmp{0};
            for (int i = 0; i < s; i++)
            {
                TreeNode *ptr = qNodes.front();
                
                tmp = ptr->val;
                if (ptr->left)
                {
                    qNodes.push(ptr->left);
                }
                if (ptr->right)
                {
                    qNodes.push(ptr->right);
                }
                qNodes.pop();
            }
            results.push_back(tmp);
        }
        return results;
    }
};
