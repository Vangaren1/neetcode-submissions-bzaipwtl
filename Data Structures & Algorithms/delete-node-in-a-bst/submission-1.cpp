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
    TreeNode *deleteNode(TreeNode *root, int key)
    {
        if (root == NULL)
        {
            return root;
        }

        if (root->val < key)
        {
            root->right = deleteNode(root->right, key);
        }
        else if (root->val > key)
        {
            root->left = deleteNode(root->left, key);
        }
        else
        {
            if (root->left == NULL && root->right == NULL)
            {
                return NULL;
            }

            if (root->left && root->right == NULL)
            {
                return root->left;
            }
            if (root->right && root->left == NULL)
            {
                return root->right;
            }

            TreeNode *curr = root->right;
            while (curr->left)
            {
                curr = curr->left;
            }
            root->val = curr->val;
            root->right = deleteNode(root->right, curr->val);
            return root;
        }
        return root;
    }
};