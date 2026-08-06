class Solution
{
private:
    int total;
    int target;
    vector<int> sides;

public:
    bool makesquare(vector<int> &matchsticks)
    {
        total = 0;
        for (auto &sticks : matchsticks)
        {
            total += sticks;
        }
        if (total % 4 != 0)
        {
            return false;
        }
        target = total / 4;
        sides = vector<int>(4, 0);
        sort(matchsticks.begin(), matchsticks.end(), greater<int>());
        if (matchsticks[0] > target)
        {
            return false;
        }
        return backtrack(0, matchsticks);
    }
    bool backtrack(int index, vector<int> &matchsticks)
    {
        if (index == matchsticks.size())
        {
            for( auto side: sides){
                if (side != target)
                {
                    return false;
                }
            }
            return true;
        }

        for (int s = 0; s < 4; s++)
        {
            if (s > 0 && sides[s] == sides[s - 1])
            {
                continue;
            }
            if (sides[s] + matchsticks[index] <= target)
            {
                sides[s] += matchsticks[index];
                if (backtrack(index + 1, matchsticks))
                {
                    return true;
                }
                sides[s] -= matchsticks[index];
            }
        }
        return false;
    }
};