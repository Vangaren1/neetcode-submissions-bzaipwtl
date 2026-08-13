class Solution {
public:
    int tribonacci(int n) {
                if (n == 0)
        {
            return 0;
        }
        if (n == 1 || n == 2)
        {
            return 1;
        }

        vector<int> tri(n + 1, 0);
        tri[1] = 1;
        tri[2] = 1;
        for (int index = 3; index < n + 1; index++)
        {
            tri[index] = tri[index - 1] + tri[index - 2] + tri[index - 3];
        }
        return tri[n];
    }
};