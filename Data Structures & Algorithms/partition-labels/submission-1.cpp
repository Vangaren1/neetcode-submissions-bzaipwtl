class Solution {
public:
    vector<int> partitionLabels(string s) {
        unordered_map<char,int> first;
        unordered_map<char,int> last;

        for(int index=0; index < s.size(); index++){
            char ch = s[index];
            if(!first.count(ch)){
                first[ch] = index;
            }
            last[ch] = index;
        }

        vector<int> results;

        for(int idx = 0; idx < s.size(); idx++){
            int start = idx;
            char startch = s[idx];
            int end = last[startch];
            while(idx < end){
                idx++;
                char tmp = s[idx];
                end = max(last[tmp], end);
            }
            results.push_back(end-start + 1);
        }
        return results;
    }
};
