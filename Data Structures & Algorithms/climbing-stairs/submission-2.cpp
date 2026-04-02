class Solution {
public:
    int climbStairs(int n) {
        vector<int> stairs(n, 0);   
        stairs[0] = 1;
        stairs[1] = 2;
        if(n==1){
            return 1;
        }
        if (n==2){
            return 2;
        }
        for(int index= 3; index < n + 1; index++){
            stairs[index - 1] = stairs[index - 2] + stairs[index - 3];
        }
        return stairs[n-1];

    }

};
