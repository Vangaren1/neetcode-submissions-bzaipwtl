class Solution {
public:
    int mySqrt(int x) {
        if (x < 2)
        {
            return x;
        }

        int left(1);
        long long curr(0), cnext(0);
        int right = x / 2;
        long long mid = left + (right - left) / 2;
        while (left < right)
        {
            curr = mid * mid;
            if (curr == x)
            {
                return mid;
            }
            cnext = (mid + 1) * (mid + 1);
            if (cnext == x)
            {
                return mid + 1;
            }
            if (curr < x)
            {
                if (cnext > x)
                {
                    return mid;
                }
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
            mid = left + (right - left) / 2;
        }
        return mid;
    }
};