class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> count = {0, 0, 0};
        for (auto &num : nums)
        {
            count[num]++;
        }
        int ptr = 0;
        for (int i = 0; i < 3; i++)
        {
            while (count[i])
            {
                nums[ptr] = i;
                count[i]--;
                ptr++;
            }
        }
    }
};