class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        int left = 0;
        int right = numbers.size() - 1;
        int currSum = numbers[left] + numbers[right];
        while (currSum != target)
        {
            if (currSum < target)
            {
                left++;
            }
            else
            {
                right--;
            }
            currSum = numbers[left] + numbers[right];
        }
        return {left + 1, right + 1};
    }
};
