class Solution {
public:
    bool canReach(string s, int minJump, int maxJump)
    {
        int n = s.size();
        if (s[n - 1] == '1')
        {
            return false;
        }

        deque<int> dq;
        dq.push_back(0);
        int farthest(0), curr(0), start(0), end(0);

        while (!dq.empty())
        {
            curr = dq.front();
            dq.pop_front();
            start = max(curr + minJump, farthest + 1);
            end = min(curr + maxJump, n - 1);
            for (int jump = start; jump < end + 1; jump++)
            {
                if (s[jump] == '0')
                {
                    if (jump == n - 1)
                    {
                        return true;
                    }
                    dq.push_back(jump);
                }
            }
            farthest = max(farthest, end);
        }
        return n == 1;
    }
};