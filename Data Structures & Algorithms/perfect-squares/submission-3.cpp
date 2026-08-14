class Solution {
public:
    int numSquares(int n) {
        vector<int> squares;

        int num = 1;
        while(num * num <= n){
            squares.push_back(num*num);
            num++;
        }
        return coinChange(squares, n);
    }
        int coinChange(vector<int>& coins, int amount) {
        vector<long long> dp(amount + 1, INT_MAX);
        dp[0] = 0;

        for (int amt = 1; amt < amount + 1; amt++)
        {
            for (auto coin : coins)
            {
                if (amt - coin >= 0)
                {
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1);
                }
            }
        }
        if (dp[amount] == INT32_MAX)
        {
            return -1;
        }
        return dp[amount];
    }
};