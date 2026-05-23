class Solution {
public:
    vector<int> countBits(int n) {
        int total = 0;
        vector<int> results;
        for(int i = 0; i <= n; i++){
            results.push_back(popcount((unsigned int) i));
        }
        return results; 
    }
};
