class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
                unordered_map<int, int> count;
        for (auto &num : nums)
        {
            count[num]++;
        }
        int k = (int)nums.size() - count[val];
        count[val]= 0;
        int ptr = 0;
        for (auto &[key, value] : count)
        {
            for (int i = 0; i < value; i++)
            {
                nums[ptr + i] = key;
            }
            ptr = ptr + value;
        }
        return k;
    }
};