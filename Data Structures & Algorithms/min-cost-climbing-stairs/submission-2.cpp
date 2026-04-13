class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int> paid(cost);

        paid.push_back(0);

        for(int index = paid.size() - 3; index > -1; index--){
            paid[index] = paid[index] + min(paid[index+1], paid[index+2]);
        }

        return min(paid[0], paid[1]);

    }
};
