class Solution
{
public:
    int splitArray(vector<int> &nums, int k)
    {
        int left(0), right(0), mid(0), pieces(0), curr(0);
        for (auto &num : nums)
        {
            left = max(left, num);
            right += num;
        }

        while (left <= right)
        {
            mid = left + (right - left) / 2;

            pieces = 1;
            curr = 0;
            for (auto &tmp : nums)
            {
                if (tmp + curr > mid)
                {
                    pieces++;
                    curr = tmp;
                }
                else
                {
                    curr += tmp;
                }
            }

            if (pieces <= k)
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }
        return left;
    }
};