class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int left = 0;
        int right = 0;
        for (auto &tmp : weights)
        {
            left = max(left, tmp);
            right += tmp;
        }

        int d(1), mid(0), curr(0);
        while (left < right)
        {
            mid = left + (right - left) / 2;
            curr = 0;
            d=1;
            for (auto &weight : weights)
            {
                if (curr + weight > mid)
                {
                    curr = weight;
                    d++;
                }
                else
                {
                    curr += weight;
                }
            }
            if (d <= days)
            {
                right = mid;
            }
            else
            {
                left = mid + 1;
            }
        }

        return left;        
    }
};