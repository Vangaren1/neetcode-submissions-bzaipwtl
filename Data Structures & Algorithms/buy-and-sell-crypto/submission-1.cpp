class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minSell = prices[0];
        int maxProfit{0}, curr{0};

        for (int num : prices)
        {
            curr = num - minSell;
            maxProfit = max(maxProfit, curr);
            minSell = min(minSell, num);
        }
        return maxProfit;
    }
};
