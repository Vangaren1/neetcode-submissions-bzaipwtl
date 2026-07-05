class Solution {
public:
    void reverseString(vector<char>& s) {
        char tmp;
        int n = s.size();
        for(int index=0; index <n/2; index++){
            tmp = s[index];
            s[index] = s[n-1-index];
            s[n-1-index] = tmp;
        }
    }
};