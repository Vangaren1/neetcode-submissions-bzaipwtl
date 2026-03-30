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
    bool isBalanced(TreeNode *root)
    {
        if (!root)
        {
            return true;
        }

        int left = maxDepth(root->left);
        int right = maxDepth(root->right);
        if (abs(left - right) > 1)
        {
            return false;
        }
        bool checkLeft = isBalanced(root->left);
        bool checkRight = isBalanced(root->right);
        return checkLeft && checkRight;
    }

    int maxDepth(TreeNode *root)
    {
        if (!root)
        {
            return 0;
        }
        int left = maxDepth(root->left);
        int right = maxDepth(root->right);
        return max(left, right) + 1;
    }
};
