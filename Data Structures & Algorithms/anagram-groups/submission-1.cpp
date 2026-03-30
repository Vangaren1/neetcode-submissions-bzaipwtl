class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
                unordered_map<string, vector<string>> dict;
        for (string st : strs)
        {
            string tmp = st;
            sort(tmp.begin(), tmp.end());
            dict[tmp].push_back(st);
        }

        vector<vector<string>> result;

        for (const auto &[key, value] : dict)
        {
            result.push_back(value);
        }
        return result;
    }
};
