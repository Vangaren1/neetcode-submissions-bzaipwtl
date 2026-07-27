class Solution
{
public:
    Node *construct(vector<vector<int>> &grid)
    {
        return recursive(grid.size(), 0, 0, grid);
    }

    Node *recursive(int n, int offsetY, int offsetX, vector<vector<int>> &grid)
    {
        if (n == 1)
        {
            return new Node(grid[offsetY][offsetX], true, nullptr, nullptr, nullptr, nullptr);
        }

        int newN = n / 2;
        Node *topleft = recursive(newN, offsetY, offsetX, grid);
        Node *topright = recursive(newN, offsetY, offsetX + newN, grid);
        Node *bottomleft = recursive(newN, offsetY + newN, offsetX, grid);
        Node *bottomright = recursive(newN, offsetY + newN, offsetX + newN, grid);

        if (topleft->isLeaf && topright->isLeaf && bottomleft->isLeaf && bottomright->isLeaf && topleft->val == topright->val && topleft->val == bottomleft->val && topleft->val == bottomright->val)
        {
            bool val = topleft->val;
            delete topleft;
            delete topright;
            delete bottomleft;
            delete bottomright;
            return new Node(val, true, nullptr, nullptr, nullptr, nullptr);
        }

        return new Node(true, false, topleft, topright, bottomleft, bottomright);
    }
};