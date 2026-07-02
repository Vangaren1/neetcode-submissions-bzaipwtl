class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int total = 0;
        for (int index = 1; index < prices.size(); index++)
        {
            if (prices[index] > prices[index - 1])
            {
                total += prices[index] - prices[index - 1];
            }
        }
        return total;
    }
};