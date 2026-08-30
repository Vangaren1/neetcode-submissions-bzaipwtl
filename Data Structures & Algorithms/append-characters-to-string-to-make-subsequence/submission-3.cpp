class Solution {
public:
    int appendCharacters(string s, string t) {
                int tPtr = 0;

        for (auto &ch : s)
        {
            if (tPtr < t.size() && ch == t[tPtr])
            {
                tPtr++;
            }
        }
        return t.size() - tPtr;
    }
};