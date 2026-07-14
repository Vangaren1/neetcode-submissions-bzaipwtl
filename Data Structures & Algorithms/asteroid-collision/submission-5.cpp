class Solution
{
public:
    vector<int> asteroidCollision(vector<int> &asteroids)
    {
        vector<int> stk;
        for (auto &asteroid : asteroids)
        {
            bool alive = true;
            while (alive && !stk.empty() && stk.back() > 0 && asteroid < 0)
            {
                if (stk.back() < -asteroid)
                {
                    stk.pop_back();
                }
                else if (stk.back() == -asteroid)
                {
                    stk.pop_back();
                    alive = false;
                }
                else
                {
                    alive = false;
                }
            }
            if (alive)
            {
                stk.push_back(asteroid);
            }
        }
        return stk;
    }
};