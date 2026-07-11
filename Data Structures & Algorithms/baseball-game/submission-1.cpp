class Solution {
public:
    int calPoints(vector<string> &operations)
    {
        stack<int> stk;
        for (auto &op : operations)
        {
            if (op == "C")
            {
                stk.pop();
            }
            else if (op == "D")
            {
                stk.push(2 * stk.top());
            }
            else if (op == "+")
            {
                int tmp = stk.top();
                stk.pop();
                int tmp2 = tmp + stk.top();
                stk.push(tmp);
                stk.push(tmp2);
            }
            else
            {
                stk.push(stoi(op));
            }
        }
        int total = 0;
        while (!stk.empty())
        {
            total += stk.top();
            stk.pop();
        }
        return total;
    }
};