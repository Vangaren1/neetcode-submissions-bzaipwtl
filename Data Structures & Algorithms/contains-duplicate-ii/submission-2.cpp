class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> curr;
        int val(0);
        for (int index = 0; index < nums.size(); index++)
        {
            val = nums[index];
            if (curr.count(val) && abs(index - curr[val]) <= k)
            {
                return true;
            }
            curr[val] = index;
        }
        return false;
    }
};