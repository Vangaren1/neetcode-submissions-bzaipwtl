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
        traverse(root, 0);
        return results;
    }

    void traverse(TreeNode *node, int level)
    {
        if (!node)
        {
            return;
        }

        if (results.size() < level+1)
        {
            results.push_back({node->val});
        }
        else
        {
            results[level].push_back(node->val);
        }

        traverse(node->left, level + 1);
        traverse(node->right, level + 1);
    }
};
