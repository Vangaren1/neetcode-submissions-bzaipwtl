class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.size()==0){
            return 0;
        }
        unordered_map<char, int> seen;
        int longest{1}, left{0}, right{1};
        seen[s[0]]=1;
        
        while( right < s.size() && left < s.size()){
            seen[s[right]]++;
            while(seen[s[right]]>1){
                seen[s[left]]--;
                left++;
            }
            longest = max(longest, right - left + 1);
            right++;
        }
    
        return longest;
    }
};
