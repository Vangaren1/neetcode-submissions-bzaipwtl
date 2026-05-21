class Solution {
public:
    bool checkValidString(string s) {
        vector<int> left;
        vector<int> star;

        for(int index= 0; index < s.size(); index++){
            char ch = s[index];
            if(ch == '('){
                left.push_back(index);
            }else if(ch == '*'){
                star.push_back(index);
            }else{
                if(left.size() > 0){
                    left.pop_back();
                }else if(star.size() > 0){
                    star.pop_back();
                }else{
                    return false;
                }
            }
        }

        if(star.size() < left.size()){
            return false;
        }

        while(!left.empty()){
            int curr = left.back();
            left.pop_back();
            if( star.back() < curr){
                return false;
            }
            star.pop_back();
        }
        return true;
    }
};
