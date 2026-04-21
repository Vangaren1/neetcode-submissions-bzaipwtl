class Solution {
public:
    string longestPalindrome(string s)
    {
        string longest;
        for (int index = 0; index < s.size(); index++)
        {
            int left = index;
            int right = index;
            if ((index + 1) < s.size() && s[index] == s[index + 1])
            {
                find(left, right + 1, s, longest);
            }
            find(left, right, s, longest);
        }
        return longest;
    }

    void find(int left, int right, string &s, string &longest)
    {
        while (left >= 0 && right < s.size() && s[left] == s[right])
        {
            string sstr = s.substr(left, right - left + 1);
            if (sstr.size() > longest.size())
            {
                longest = sstr;
            }
            left--;
            right++;
        }
    }
};
