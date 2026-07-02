class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
                int cand1(INT32_MIN);
        int cand2(INT32_MIN);
        int count1(0), count2(0);
        for (auto &num : nums)
        {
            if (num == cand1)
            {
                count1++;
            }
            else if (num == cand2)
            {
                count2++;
            }
            else if (count1 == 0)
            {
                cand1 = num;
                count1 = 1;
            }
            else if (count2 == 0)
            {
                cand2 = num;
                count2 = 1;
            }
            else
            {
                count1--;
                count2--;
            }
        }
        vector<int> results;
        int n = nums.size();

        if (cand1 != INT32_MAX)
        {
            int cand1Count = count(nums.begin(), nums.end(), cand1);
            if (cand1Count * 3 > n)
            {
                results.push_back(cand1);
            }
        }

        if (cand2 != INT32_MAX)
        {
            int cand2Count = count(nums.begin(), nums.end(), cand2);
            if (cand2Count * 3 > n)
            {
                results.push_back(cand2);
            }
        }
        return results;
    }
};