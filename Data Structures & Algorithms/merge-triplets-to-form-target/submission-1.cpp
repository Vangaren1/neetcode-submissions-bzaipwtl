class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        bool a = false;
        bool b = false;
        bool c = false;

        for (const auto &tmp : triplets)
        {
            int first = tmp[0];
            int second = tmp[1];
            int third = tmp[2];
            if (first > target[0] || second > target[1] || third > target[2])
            {
                continue;
            }
            if(first == target[0]){
                a = true;
            }
            if(second == target[1]){
                b = true;
            }
            if(third == target[2]){
                c = true;
            }
            if(a && b && c){
                break;
            }
        }
        return a && b && c;
    }
};
