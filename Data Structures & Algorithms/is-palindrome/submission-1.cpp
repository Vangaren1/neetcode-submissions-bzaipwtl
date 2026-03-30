class Solution {
public:
    bool isPalindrome(string s)
    {

        string tmp;
        for (char ch : s)
        {
            if (isalnum(ch))
            {
                tmp += tolower(ch);
            }
        }
        int start = 0;
        int end = tmp.size()-1;
        while (start <= end)
        {
            if (tmp[start] != tmp[end])
            {
                return false;
            }

            start++;
            end--;
        }
        return true;
    }
};
