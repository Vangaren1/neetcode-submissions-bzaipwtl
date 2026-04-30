class Solution
{
private:
    unordered_set<int> seen;
    unordered_set<int> checking;
    vector<int> order;    
    vector<vector<int>> courses;
public:
    vector<int> findOrder(int numCourses, vector<vector<int>> &prerequisites)
    {
        courses = vector<vector<int>>(numCourses);
        for(vector<int> prereq : prerequisites){
            courses[prereq[0]].push_back(prereq[1]);
        }

        vector<int> emp; 
        for(int c = 0; c < numCourses; c++){
            if(!dfs(c)){
                
                return emp;
            }else{
                courses[c]=emp;
            }
        }
        return order;
    }
    bool dfs(int c){
        if(checking.count(c)){
            return false;
        }
        if(seen.count(c)){
            return true;
        }
        checking.insert(c);

        for(int pre : courses[c]){
            if(!dfs(pre)){
                return false;
            }
        }
        checking.erase(c);
        seen.insert(c);
        order.push_back(c);
        return true;
    }
};