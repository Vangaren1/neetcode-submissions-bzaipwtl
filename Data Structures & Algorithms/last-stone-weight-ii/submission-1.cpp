
class Solution
{
private:
    struct PairHash
    {
        size_t operator()(const pair<int, int> &p) const
        {
            return hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
        }
    };

    unordered_map<pair<int, int>, int, PairHash> memo;
    int stonesum;
    int target;

public:
    int lastStoneWeightII(vector<int> &stones)
    {
        memo.clear();
        stonesum = 0;
        for (auto stone : stones)
        {
            stonesum += stone;
        }
        target = (stonesum) / 2;
        return dfs(0, 0, stones);
    }
    int dfs(int index, int total, vector<int> &stones)
    {
        if (index >= stones.size() || total >= target)
        {
            return abs(total - (stonesum - total));
        }
        if (memo.count({index, total}))
        {
            return memo[{index, total}];
        }

        int take1 = dfs(index + 1, total + stones[index], stones);
        int donttake1 = dfs(index + 1, total, stones);
        memo[{index, total}] = min(take1, donttake1);
        return memo[{index, total}];
    }
};