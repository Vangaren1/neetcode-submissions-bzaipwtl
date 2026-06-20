class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<pair<int,int>> stack;
        vector<int> results(n, 0);

        for(int index = 0; index < n; index++){
            int temp = temperatures[index];

            while(!stack.empty() && stack.back().second < temp){
                auto tmp = stack.back();
                stack.pop_back();
                results[tmp.first] = index - tmp.first;
            }
            stack.push_back({index, temp});

        }
        return results;
    }
};
