class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // find the max value
        auto rIdx = max_element(piles.begin(), piles.end());
        int right = rIdx - piles.begin();
        right = piles[right];

        int left{1}, mid{-1}, total{-1};
        // use binary search to find the min
        while (left < right)
        {
            mid = (left + right) / 2;
            total = 0;
            for (int p : piles)
            {
                total +=  (p + mid - 1)/ mid;
            }

            if (total <= h)
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
