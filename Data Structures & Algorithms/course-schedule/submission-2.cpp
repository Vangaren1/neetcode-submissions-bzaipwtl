class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> courses(numCourses);

        for (vector<int>& curr : prerequisites) {
            int a = curr[0];
            int b = curr[1];
            courses[a].push_back(b);
        }

        unordered_set<int> checking; // current DFS path
        unordered_set<int> checked;  // already proven safe

        for (int c = 0; c < numCourses; c++) {
            if (!dfs(c, courses, checking, checked)) {
                return false;
            }
        }

        return true;
    }

    bool dfs(
        int course,
        vector<vector<int>>& courses,
        unordered_set<int>& checking,
        unordered_set<int>& checked
    ) {
        if (checking.count(course)) {
            return false; // cycle
        }

        if (checked.count(course)) {
            return true; // already verified safe
        }

        checking.insert(course);

        for (int pre : courses[course]) {
            if (!dfs(pre, courses, checking, checked)) {
                return false;
            }
        }

        checking.erase(course);
        checked.insert(course);

        return true;
    }
};