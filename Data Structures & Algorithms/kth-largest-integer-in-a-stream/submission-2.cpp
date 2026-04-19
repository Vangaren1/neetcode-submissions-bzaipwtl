class KthLargest
{
private:
    priority_queue<int, std::vector<int>, std::greater<int>> minQ;
    int kItems;

public:
    KthLargest(int k, vector<int> &nums)
    {
        kItems = k;
        for (int n : nums)
        {
            minQ.push(n);
            if (minQ.size() > k)
            {
                minQ.pop();
            }
        }
    }

    int add(int val)
    {
        minQ.push(val);
        if (minQ.size() > kItems)
        {
            minQ.pop();
        }
        return minQ.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */