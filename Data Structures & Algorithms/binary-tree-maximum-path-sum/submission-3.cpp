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
int maxPathSum(TreeNode *root)
    {
        int maxFound = INT_MIN;
        dfs(root, maxFound);
        return maxFound;
    }

    int dfs(TreeNode *root, int &maxFound)
    {
        if (!root)
        {
            return 0;
        }

        int left = dfs(root->left, maxFound);
        int right = dfs(root->right, maxFound);

        int maxChild = max(left, max(right, 0));
        int nPlusChild = root->val + maxChild;
        int split = left + right + root->val;
        maxFound = max({maxFound, split, nPlusChild, root->val});
        return nPlusChild;
    }
};
