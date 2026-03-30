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
        vector<int> arr;
        dfs(root, k, arr);
        return arr[k-1];
    }
    void dfs(TreeNode *node, int k, vector<int> &arr)
    {
        if(node){
        dfs(node->left, k, arr);
        if (arr.size() < k)
        {
            arr.push_back(node->val);
        }
        else
        {
            return;
        }
        dfs(node->right, k, arr);
        }

    }
};