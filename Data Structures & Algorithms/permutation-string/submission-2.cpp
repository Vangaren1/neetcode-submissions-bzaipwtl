class Solution {
public:
    bool checkInclusion(string s1, string s2)
    {
        if(s2.size() < s1.size()){return false;}
        vector<int> count(26, 0), window(26, 0);

        for (char ch : s1)
        {
            count[ch - 'a']++;
        }

        int left{0}, right{0};

        while (right < s1.size())
        {
            window[s2[right] - 'a']++;
            right++;
        }

        while (right < s2.size())
        {
            if (matches(count, window))
            {
                return true;
            }


            window[s2[right] - 'a']++;
            window[s2[left] - 'a']--;
            right++;
            left++;
        }
        return matches(count, window);
    }

    bool matches(vector<int> a, vector<int> b)
    {
        for (int index = 0; index < a.size(); index++)
        {
            if (b[index] != a[index])
            {
                return false;
            }
        }
        return true;
    }
};