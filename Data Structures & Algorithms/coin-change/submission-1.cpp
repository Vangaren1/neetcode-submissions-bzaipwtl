class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<long long> dp( amount+1, INT_MAX);
        dp[0]=0;

        for(int amt=1; amt < amount +1 ; amt++){
            for(int c : coins){
                if(c <= amt){
                    dp[amt] = min(dp[amt], dp[amt-c]+1);
                }
            }
        }
        if(dp[amount]<INT_MAX){
            return dp[amount];
        }
        return -1;
    }
};