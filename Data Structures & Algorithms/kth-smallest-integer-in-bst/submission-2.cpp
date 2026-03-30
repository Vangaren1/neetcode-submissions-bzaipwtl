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
        int kthSmallest(TreeNode *root, int k)
    {
        int val{0};
        dfs(root, k, val);
        return val;
    }
    void dfs(TreeNode *node, int &k, int &v)
    {
        if (!node || k == 0)
        {
            return;
        }
        dfs(node->left, k, v);
        if (k == 0)
            return;

        k--;
        if (k == 0)
        {
            v = node->val;
            return;
        }
        dfs(node->right, k, v);
    }
};