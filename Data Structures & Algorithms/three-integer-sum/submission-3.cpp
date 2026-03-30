class Solution {
public:
    struct Triple
    {
        int a, b, c;

        bool operator<(const Triple &other) const
        {
            if (a != other.a)
                return a < other.a;
            if (b != other.b)
                return b < other.b;
            return c < other.c;
        }
    };

    vector<vector<int>> threeSum(vector<int> &nums)
    {
        set<Triple> s;
        vector<vector<int>> results;
        int n = nums.size();
        sort(nums.begin(), nums.end());

        int left{0}, right{0}, check{0};

        for (int index = 1; index < n; index++)
        {
            left = 0;
            right = n - 1;

            while (left < index && right > index)
            {
                check = nums[index] + nums[left] + nums[right];

                if (check == 0)
                {
                    s.insert({nums[left], nums[index], nums[right]});
                    left++;
                }
                else if (check < 0)
                {
                    left++;
                }
                else if (check > 0)
                {
                    right--;
                }
            }
        }

        for (Triple tmp : s)
        {
            results.push_back({tmp.a, tmp.b, tmp.c});
        }

        return results;
    }
};
