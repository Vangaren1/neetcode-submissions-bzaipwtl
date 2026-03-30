class Solution
{
public:
        string minWindow(string s, string t)
    {
        if (s.size() < t.size())
        {
            return "";
        }

        vector<int> chCnt(52, 0);
        vector<int> tCnt(52, 0);
        string minStr{""}, window{""};
        int left{0}, right{0};

        for (char ch : t)
        {
            incrementV(ch, tCnt);
        }

        char tmp{'a'};

        minStr = "";

        while (left < s.size())
        {
            while (right < s.size() && !contains(chCnt, tCnt))
            {
                incrementV(s[right], chCnt);
                right++;
            }
            if (right <= s.size() && contains(chCnt, tCnt) && (minStr.empty() || minStr.size() > (right - left)))
            {
                minStr = s.substr(left, right - left);
            }

            decrementV(s[left], chCnt);
            left++;
        }
        return minStr;
    }

    void incrementV(char &ch, vector<int> &v)
    {
        if (islower(ch))
        {
            v[ch - 'a']++;
        }
        else
        {
            v[ch - 'A' + 26]++;
        }
    }

    void decrementV(char &ch, vector<int> &v)
    {
        if (islower(ch))
        {
            v[ch - 'a']--;
        }
        else
        {
            v[ch - 'A' + 26]--;
        }
    }
    bool contains(vector<int> &A, vector<int> &B)
    {
        for (int index = 0; index < A.size(); index++)
        {
            if (A[index] < B[index])
            {
                return false;
            }
        }
        return true;
    }
};
