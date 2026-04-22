class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int, vector<int>>> distList;
        for (vector<int> point : points)
        {
            int dist = point[0] * point[0] + point[1] *point[1];
            pair<int, vector<int>> tmp = {dist, point};
            distList.push(tmp);
            if (distList.size() > k)
            {
                distList.pop();
            }
        }

        vector<vector<int>> results;
        while (!distList.empty())
        {
            results.push_back(distList.top().second);
            distList.pop();
        }
        return results;
    }
};
