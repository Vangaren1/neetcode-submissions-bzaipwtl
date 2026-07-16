class FreqStack
{
private:
    unordered_map<int, int> freq;
    unordered_map<int, vector<int>> groups;
    int maxFreq;

public:
    FreqStack()
    {
        maxFreq = 0;
    }

    void push(int val)
    {
        freq[val]++;
        groups[freq[val]].push_back(val);
        maxFreq = max(maxFreq, freq[val]);
    }

    int pop()
    {
        int val = groups[maxFreq].back();
        groups[maxFreq].pop_back();
        freq[val]--;
        if (groups[maxFreq].size() == 0)
        {
            maxFreq--;
        }
        return val;
    }
};


/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */