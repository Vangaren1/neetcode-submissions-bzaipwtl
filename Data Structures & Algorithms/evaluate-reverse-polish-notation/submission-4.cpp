
class Solution
{
public:
    int evalRPN(vector<string> &tokens)
    {
        unordered_set<string> oprs = {"+", "-", "*", "/"};
        vector<int> stk;
        int a, b;
        for (string tk : tokens)
        {
            if (!oprs.count(tk))
            {
                stk.push_back(stoi(tk));
                continue;
            }
            a = stk.back();
            stk.pop_back();
            b = stk.back();
            stk.pop_back();

            if (tk == "+")
            {
                stk.push_back(a + b);
            }
            else if (tk == "-")
            {
                stk.push_back(b - a);
            }
            else if (tk == "*")
            {
                stk.push_back(b * a);
            }
            else if (tk == "/")
            {
                stk.push_back(b / a);
            }
        }

        return stk.back();
    }
};
