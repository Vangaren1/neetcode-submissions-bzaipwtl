
class MinStack
{
private:
    vector<pair<int, int>> stk;

public:
    MinStack()
    {
    }

    void push(int val)
    {
        if (stk.size() > 0)
        {
            int t = getMin();
            stk.push_back({val, min(val, t)});
        }else{
            stk.push_back({val,val});
        }
    }

    void pop()
    {
        if(stk.size()>0){
            stk.pop_back();
        }
    }

    int top()
    {
        pair<int, int> tmp = stk.back();
        return tmp.first;
    }

    int getMin()
    {
        pair<int, int> tmp = stk.back();
        return tmp.second;
    }
};
