class Solution {
public:
    int carFleet(int target, vector<int> &position, vector<int> &speed)
    {
        vector<pair<int,int>> highway;

        for(int index=0; index < position.size(); index++){
            highway.push_back({position[index], speed[index]});
        }
        sort(highway.rbegin(), highway.rend());

        vector<pair<int,int>> carStack;

        for(pair<int,int> car : highway){
            if(carStack.empty()){
                carStack.push_back(car);
                continue;
            }

            if(!collide(target, car, carStack.back())){
                carStack.push_back(car);
            }
        }

        return carStack.size();
    }

    bool collide(int target, pair<int, int> a, pair<int, int> b){
        double arriveA = (double)(target - a.first) / a.second;
        double arriveB = (double)(target - b.first) / b.second;
        return arriveA <= arriveB;
    }
};
