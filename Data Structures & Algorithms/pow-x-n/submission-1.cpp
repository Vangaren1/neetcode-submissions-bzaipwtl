class Solution {
public:
    double myPow(double x, int n) {
        if(x==0){
            return 0;
        }
        if(n==0){
            return 1;
        }
        if(n==1){
            return x;
        }

        if(n<0){
            return 1.0 / myPow(x, abs(n));
        }

        if(n % 2 == 0){
            double result = myPow(x, n /2);
            return result * result;
        }

        return myPow(x, n-1) * x;
    }
};
