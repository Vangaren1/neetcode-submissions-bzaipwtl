class Solution {
public:
    bool isAnagram(string s, string t)
    {
        if(s.size() != t.size()){
            return false;
        }
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        for(int idx = 0; idx < s.size(); idx++){
            if(s[idx] != t[idx]){return false;}
        }
        return true;
    }
};
