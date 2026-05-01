class Solution {
    private:
unordered_map<int,vector<int>> adj;
unordered_set<int> visited;
public:
    bool validTree(int n, vector<vector<int>> &edges)
    {
        if(edges.size() != (n-1)){
            return false;
        }
        for(vector<int> uv : edges){
            adj[uv[0]].push_back(uv[1]);
            adj[uv[1]].push_back(uv[0]);
        }
        bool check = dfs(0,-1);

        return check && visited.size() == n;
    }

    bool dfs(int v, int parent){
        if(visited.count(v)){
            return false;
        }
        visited.insert(v);
        for(int neighbor : adj[v]){
            if(neighbor == parent){
                continue;
            }
            if(!dfs(neighbor, v)){
                return false;
            }
        }
        return true;
    }

};
