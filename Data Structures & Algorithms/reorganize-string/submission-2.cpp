class Solution
{
public:
    string reorganizeString(string s)
    {
        unordered_map<char, int> count;
        int maxCount = -1;
        for (auto &ch : s)
        {
            count[ch]++;
            maxCount = max(maxCount, count[ch]);
        }

        if (maxCount > (s.size() + 1) / 2)
        {
            return "";
        }

        priority_queue<pair<int, char>> pq;
        for (const auto &[key, value] : count)
        {
            pq.push({value, key});
        }

        string result = "";
        pair<int, char> prev = {-1, 'n'};

        while (!pq.empty())
        {
            pair<int, char> tmp = pq.top();
            pq.pop();

            result = result + tmp.second;
            tmp.first--;

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
                prev = {-1, 'n'};
            }
        }
        return result;
    }
};