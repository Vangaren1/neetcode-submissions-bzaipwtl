class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<int> dp(amount+1, 0);
        dp[0]=1;

        for(int coin : coins){
            for(int index=coin; index < amount+1; index++){
                dp[index] = dp[index] + dp[index-coin];
            }
        }
        return dp[amount];

    }
};
