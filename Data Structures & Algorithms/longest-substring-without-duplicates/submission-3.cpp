class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        unordered_map<char, int> seen;
        int longest{0}, left{0}, right{0};
        
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
