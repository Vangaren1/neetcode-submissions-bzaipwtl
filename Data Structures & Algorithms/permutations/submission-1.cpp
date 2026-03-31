class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
         vector<vector<int>> results;

        if (nums.size() == 0)
        {
            return results;
        }

        if (nums.size() == 1)
        {
            results.push_back(nums);
            return results;
        }

        for (int index = 0; index < nums.size(); index++)
        {
            vector<int> arr = nums;
            int curr = arr[index];
            arr.erase(arr.begin() + index);
            vector<vector<int>> tmp = permute(arr);

            for (vector<int> sub : tmp)
            {
                sub.insert(sub.begin(), curr);
                results.push_back(sub);
            }
        }
        return results;
    }
};
