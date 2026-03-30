class Solution {
public:
    bool isValid(string s)
    {
        unordered_map<char, char> parans = {
            {')', '('},
            {'}', '{'},
            {']', '['}};

        unordered_set<char> opn = {'(', '[', '{'};
        vector<char> stk;
        for( char ch : s){
            if(opn.count(ch)>0){
                stk.push_back(ch);
            }else{
                if(stk.size() == 0 || parans[ch]!=stk.back()){
                    return false;
                }
                stk.pop_back();
            }
        }

        return stk.size() == 0;
    }
};
