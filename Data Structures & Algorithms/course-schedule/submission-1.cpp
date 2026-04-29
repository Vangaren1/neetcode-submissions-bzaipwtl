class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>> &prerequisites)
    {
        vector<vector<int>> courses(numCourses);
        for (vector<int> curr : prerequisites)
        {
            int a = curr[0];
            int b = curr[1];
            courses[a].push_back(b);
        }

        unordered_set<int> checking;

        for (int c = 0; c < numCourses; c++)
        {
            if (!dfs(c, courses, checking, prerequisites))
            {
                return false;
            }
        }
        return true;
    }

    bool dfs(int course, vector<vector<int>> &courses, unordered_set<int> &checking, vector<vector<int>> &prerequisites)
    {
        if (checking.count(course))
        {
            return false;
        }

        checking.insert(course);

        for (int pre : courses[course])
        {
            if (!dfs(pre, courses, checking, prerequisites))
            {
                return false;
            }
        }

        checking.erase(course);
        return true;
    }
};
