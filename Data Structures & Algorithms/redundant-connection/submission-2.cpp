
class QUFind
{
private:
    vector<int> arr;

public:
    QUFind(int n)
    {
        for (int i = 0; i < n; i++)
        {
            arr.push_back(i);
        }
    }

    bool connected(int a, int b){
        return arr[a]==arr[b];
    }

    bool quUnion(int a, int b){
        int currA = arr[a];
        int currB = arr[b];
        if (currA == currB){
            return false;
        }
        for(int i = 0; i < arr.size(); i++){
            if(arr[i]==currA){
                arr[i] = currB;
            }
        }
        return true;
    }

    int getArr(){
        unordered_set<int> compSet;
        for( int tmp : arr){
            compSet.insert(tmp);
        }
        return compSet.size();
    }
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int mA(INT32_MIN), mB(INT32_MIN);
        for(vector<int> ab : edges){
            if(ab[0] > mA){
                mA = ab[0];
            }
            if(ab[1] > mB){
                mB = ab[1];
            }
        }
        QUFind qu = QUFind(max(mA, mB)+1);
        for(vector<int> edge : edges){
            bool check = qu.quUnion(edge[0], edge[1]);
            if(!check){
                return edge;
            }
        }
    }
};