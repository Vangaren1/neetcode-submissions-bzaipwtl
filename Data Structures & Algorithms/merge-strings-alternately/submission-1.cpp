class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int ptr1(0), ptr2(0);
        string result;
        while (ptr1 < word1.size() && ptr2 < word2.size())
        {
            result += word1[ptr1];
            result += word2[ptr2];
            ptr1++;
            ptr2++;
        }
        if (ptr1 < word1.size())
        {
            return result + word1.substr(ptr1, word1.size());
        }
        return result + word2.substr(ptr2, word2.size());
    }
};