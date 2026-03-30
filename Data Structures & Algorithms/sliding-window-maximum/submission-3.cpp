class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
             priority_queue<pair<int, int>> maxQ;
        vector<int> results;

        int left{0};
        int n = nums.size();

        for (int right = 0; right < n; right++)
        {

            maxQ.push({nums[right], right});
            left = right - k + 1;

            if (left >= 0)
            {

                while (maxQ.top().second < left)
                {
                    maxQ.pop();
                }
                results.push_back(maxQ.top().first);
            }
        }

        return results;
   
    }
};
