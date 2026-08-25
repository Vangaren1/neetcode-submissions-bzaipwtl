class Solution {
public:
    int candy(vector<int>& ratings) {
                int n = ratings.size();
        vector<int> results(n, 1);
        for(int index = 1; index < n; index++){
            if(ratings[index] > ratings[index-1]){
                results[index] = results[index-1] +1;
            }
        }
        for(int i = n-2; i > -1; i--){
            if(ratings[i] > ratings[i+1]){
                results[i] = max(results[i], results[i+1]+1);
            }
        }
        int total = 0;
        for(int j = 0; j < n; j++){
            total += results[j];
        }
        return total;
    }
};