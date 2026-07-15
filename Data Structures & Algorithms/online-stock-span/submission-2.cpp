class StockSpanner
{
private:
    vector<pair<int, int>> stk;

public:
    StockSpanner()
    {
    }

    int next(int price)
    {
        int span = 1;
        while (!stk.empty() && stk.back().first <= price)
        {
            auto tmp = stk.back();
            stk.pop_back();
            span += tmp.second;
        }
        stk.push_back({price, span});
        return span;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */