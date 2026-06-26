class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        for(int index=0; index < strs[0].size(); index++){
            for( auto&s : strs){
                if(s.size()-1 < index || s[index]!=strs[0][index]){
                    return s.substr(0,index);
                }
            }
        }
        return strs[0];
    }
};