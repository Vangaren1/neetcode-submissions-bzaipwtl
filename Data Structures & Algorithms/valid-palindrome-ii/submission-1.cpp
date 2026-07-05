class Solution
{
public:
    bool validPalindrome(string s)
    {
        int left(0);
        int right = s.size() - 1;
        while (left < right)
        {
            if (s[left] != s[right])
            {
                return palinSkip(s, left) || palinSkip(s, right);
            }
            left++;
            right--;
        }
        return true;
    }
    bool palinSkip(string s, int n)
    {
        int left(0);
        int right = s.size() - 1;
        while (left < right)
        {
            if (left == n)
            {
                left++;
            }
            else if (right == n)
            {
                right--;
            }
            if (s[left] != s[right])
            {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};