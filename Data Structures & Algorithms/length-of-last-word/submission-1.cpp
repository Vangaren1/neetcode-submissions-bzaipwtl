class Solution {
public:
    int lengthOfLastWord(string s) {
        int last = 0;
        stringstream ss(s);
        string word;
        while( ss >> word){
            last = word.size();
        }

        return last;
    }
};