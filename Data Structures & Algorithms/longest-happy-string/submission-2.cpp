class Solution
{
public:
    string longestDiverseString(int a, int b, int c)
    {
        string s = "";

        int total = a + b + c;
        priority_queue<pair<int, char>> pq;
        if (a > 0)
        {
            pq.push({a, 'a'});
        }
        if (b > 0)
        {
            pq.push({b, 'b'});
        }
        if (c > 0)
        {
            pq.push({c, 'c'});
        }

        pair<int, char> prev = {-1, 'n'};
        while (!pq.empty())
        {
            auto tmp = pq.top();
            pq.pop();

            int others = total - tmp.first;
            if (tmp.first > others and tmp.first > 1)
            {
                s += tmp.second;
                s += tmp.second;
                tmp.first = tmp.first - 2;
                total = total - 2;
            }
            else
            {
                s += tmp.second;
                tmp.first--;
                total--;
            }

            if (prev.first != -1)
            {
                pq.push(prev);
            }

            if (tmp.first > 0)
            {
                prev = tmp;
            }
            else
            {
                prev = {-1, 'c'};
            }
        }
        return s;
    }
};