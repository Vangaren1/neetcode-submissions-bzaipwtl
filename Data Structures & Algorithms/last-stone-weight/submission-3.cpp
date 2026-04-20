class Solution {
public:
    int lastStoneWeight(vector<int> &stones)
    {
        priority_queue<int> pile;
        for (int stone : stones)
        {
            pile.push(stone);
        }
        while (pile.size() > 1)
        {
            int first = pile.top();
            pile.pop();
            int second = pile.top();
            pile.pop();
            if (first == second)
            {
                continue;
            }
            pile.push(abs(first - second));
        }
        if (pile.size() == 0)
        {
            return 0;
        }
        return pile.top();
    }
};
