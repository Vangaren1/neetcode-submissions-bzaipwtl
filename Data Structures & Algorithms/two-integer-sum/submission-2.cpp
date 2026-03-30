class Solution {
public:
vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> pos;
        int tmp = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            tmp = nums[i];
            pos[target - tmp] = i;
        }

        for (int j = 0; j < nums.size(); j++)
        {
            tmp = nums[j];
            if (pos.find(tmp) != pos.end() && pos[tmp] != j)
            {
                return {j, pos[tmp]};
            }
        }
        return {};
    }
};
