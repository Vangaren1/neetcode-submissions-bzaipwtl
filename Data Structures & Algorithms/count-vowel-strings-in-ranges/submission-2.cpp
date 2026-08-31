class Solution {
public:
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
                unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        vector<int> dp = {0};

        for( auto& word : words){
            int valid = 0;
            if( vowels.count(word[0]) > 0 && vowels.count(word[word.size() -1 ])>0 ){
                valid = 1;
            }
            dp.push_back( dp.back() + valid);
        }

        vector<int> results; 

        for( auto&tmp : queries){
            int left = tmp[0];
            int right = tmp[1];

            results.push_back( dp[right + 1] - dp[left]);

        }
        return results;
    }
};