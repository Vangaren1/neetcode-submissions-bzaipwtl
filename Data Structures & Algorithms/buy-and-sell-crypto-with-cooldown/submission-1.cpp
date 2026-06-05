using namespace std;

class Solution
{
    struct PairHash
    {
        size_t operator()(const pair<int, bool> &p) const
        {
            size_t h1 = hash<int>{}(p.first);
            size_t h2 = hash<bool>{}(p.second);

            return h1 ^ (h2 << 1);
        }
    };

public:
    int maxProfit(vector<int> &prices)
    {
        unordered_map<pair<int, bool>, int, PairHash> cache;
        return rec(0, true, prices, cache);
    }

    int rec(
        int index,
        bool canBuy,
        vector<int> &prices,
        unordered_map<pair<int, bool>, int, PairHash> &c
    )
    {
        if (index >= prices.size())
        {
            return 0;
        }

        if (c.count({index, canBuy}))
        {
            return c[{index, canBuy}];
        }

        int cool = rec(index + 1, canBuy, prices, c);

        int buyOrSell;

        if (canBuy)
        {
            buyOrSell = rec(index + 1, false, prices, c) - prices[index];
        }
        else
        {
            buyOrSell = rec(index + 2, true, prices, c) + prices[index];
        }

        c[{index, canBuy}] = max(cool, buyOrSell);
        return c[{index, canBuy}];
    }
};