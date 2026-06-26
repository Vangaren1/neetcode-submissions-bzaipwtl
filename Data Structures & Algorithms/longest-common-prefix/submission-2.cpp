class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix;
        int length = INT_MAX;
        for (auto &s : strs)
        {
            length = min(length, (int)s.size());
        }

        for (int index = 0; index < length; index++)
        {
            for (auto &s : strs)
            {
                if (s[index] != strs[0][index])
                {
                    prefix = s.substr(0, index);
                    return prefix;
                }
            }
            prefix = strs[0].substr(0, index + 1);
        }
        return prefix;
    }
};