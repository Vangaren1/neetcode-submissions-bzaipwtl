class Solution {
public:
    string predictPartyVictory(string senate) {
        deque<int> rq;
        deque<int> dq;
        int n = senate.size();

        for(int i=0; i < n; i++){
            if(senate[i]=='R'){
                rq.push_back(i);
            }else{
                dq.push_back(i);
            }
        }

        while(!rq.empty() && !dq.empty()){
            int r = rq.front();
            rq.pop_front();
            int d = dq.front();
            dq.pop_front();

            if(r < d){
                rq.push_back(r + n);
            }else{
                dq.push_back(d + n);
            }
        }
        if(!rq.empty()){
            return "Radiant";
        }
        return "Dire";
    }
};