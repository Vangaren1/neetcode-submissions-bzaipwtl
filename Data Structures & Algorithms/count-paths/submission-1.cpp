class Solution {
public:
    int uniquePaths(int m, int n)
    {
              int a = m - 1;
        int b = n - 1;
        return (int)comb(a + b, b);
    }
    int comb(int a, int b)
    {
        if (b < 0 or b > a)
        {
            return 0;
        }
        if (b == 0 || b == a)
        {
            return 1;
        }
        b = min(b, a-b);
        long long result = 1;
        for (int i = 1; i <= b; i++)
        {
            result = result * (a - b + i) / i;
        }
        return result;
    }
};
