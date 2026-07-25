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
    vector<int> inorderTraversal(TreeNode *root)
    {
        vector<int> results;
        trav(root, results);
        return results;
    }

    void trav(TreeNode *node, vector<int> &res)
    {
        if (node)
        {
            trav(node->left, res);
            res.push_back(node->val);
            trav(node->right, res);
        }
    }
};