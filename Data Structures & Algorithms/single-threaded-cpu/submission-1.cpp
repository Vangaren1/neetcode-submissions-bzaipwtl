class Solution {
public:
    vector<int> getOrder(vector<vector<int>> &tasks)
    {
        vector<vector<int>> taskList;
        for (int idx = 0; idx < tasks.size(); idx++)
        {
            int startTime = tasks[idx][0];
            int duration = tasks[idx][1];
            taskList.push_back({startTime, duration, idx});
        }

        sort(taskList.begin(), taskList.end());
        int n = taskList.size();
        int time(0), index(0), ptime(0), orgIndex(0);

                priority_queue<pair<int, int>, vector<pair<int, int>>,
                       greater<pair<int, int>>>
            available;
        vector<int> result;

        while (index < n || !available.empty())
        {
            if (available.empty() && time < taskList[index][0])
            {
                time = taskList[index][0];
            }

            while (index < n && taskList[index][0] <= time)
            {
                ptime = taskList[index][1];
                orgIndex = taskList[index][2];
                available.push({ptime, orgIndex});
                index++;
            }

            auto tmp = available.top();
            available.pop();
            result.push_back(tmp.second);
            time += tmp.first;
        }
        return result;
    }
};