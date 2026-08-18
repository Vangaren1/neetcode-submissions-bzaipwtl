class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> roman = {{'I', 1},
                                          {'V', 5},
                                          {'X', 10},
                                          {'L', 50},
                                          {'C', 100},
                                          {'D', 500},
                                          {'M', 1000}};

        int total = 0;

        for (int index = 0; index < s.size(); index++)
        {
            if (index < s.size() - 1 && roman[s[index]] < roman[s[index + 1]])
            {
                total -= roman[s[index]];
            }
            else
            {
                total += roman[s[index]];
            }
        }
        return total;
    }
};