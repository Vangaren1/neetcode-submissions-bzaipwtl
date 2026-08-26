class Solution
{
public:
    int mostBooked(int n, vector<vector<int>> &meetings)
    {

        sort(meetings.begin(), meetings.end());
        vector<int> roomCount(n, 0);
        priority_queue<int, vector<int>, greater<int>> available;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> occupied;

        for (int i = 0; i < n; i++)
        {
            available.push(i);
        }

        int freeTime(0), room(0);
        for (const auto &meeting : meetings)
        {
            int start = meeting[0];
            int end = meeting[1];
            int duration = end - start;
            while (!occupied.empty() && occupied.top().first <= start)
            {
                auto [freeTime, tmproom1] = occupied.top();
                room = tmproom1;
                occupied.pop();
                available.push(room);
            }

            if (!available.empty())
            {
                room = available.top();
                available.pop();
                occupied.push({end, room});
            }
            else
            {
                auto [freeTime, tmpRoom2] = occupied.top();
                occupied.pop();
                room = tmpRoom2;
                occupied.push({freeTime + duration, room});
            }
            roomCount[room] += 1;
        }
        return max_element(roomCount.begin(), roomCount.end()) - roomCount.begin();
    }
};