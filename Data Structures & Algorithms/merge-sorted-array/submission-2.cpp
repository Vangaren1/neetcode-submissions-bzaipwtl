class Solution {
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        m--;
        n--;
        for (int index = nums1.size()-1; index >= 0; index--)
        {
            if (m >= 0 && n >= 0)
            {
                if (nums1[m] >= nums2[n])
                {
                    nums1[index] = nums1[m];
                    m--;
                }
                else
                {
                    nums1[index] = nums2[n];
                    n--;
                }
            }
            else
            {
                if (n >= 0)
                {
                    nums1[index] = nums2[n];
                    n--;
                }
            }
        }
    }
};