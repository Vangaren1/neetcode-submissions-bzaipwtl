class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left{0}, maxSeen{0}, curr{0}, lVal{0}, rVal{0};
        int right = heights.size() - 1;

        while (left < right)
        {
            lVal = heights[left];
            rVal = heights[right];
            curr = (right - left) * min(lVal, rVal);
            maxSeen = max(maxSeen, curr);

            if (lVal <= rVal)
            {
                left++;
            }
            else
            {
                right--;
            }
        }
        return maxSeen;
    }
};
