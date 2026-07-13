
class MyQueue
{
private:
    stack<int> mystack;

public:
    MyQueue()
    {
    }

    void push(int x)
    {
        stack<int> tmp;
        while (!mystack.empty())
        {
            tmp.push(mystack.top());
            mystack.pop();
        }
        mystack.push(x);
        while (!tmp.empty())
        {
            mystack.push(tmp.top());
            tmp.pop();
        }
    }

    int pop()
    {
        int n = mystack.top();
        mystack.pop();
        return n;
    }

    int peek()
    {
        return mystack.top();
    }

    bool empty()
    {
        return mystack.empty();
    }
};
