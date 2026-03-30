class Solution {
public:
    int evalRPN(vector<string>& tokens) 
    {
        unordered_set<string> oprs = {"+","-","*","/"};
        vector<string> stk; 
        int a, b;
        for( string tk : tokens){
            if(!oprs.count(tk)>0){
                stk.push_back(tk);
                continue;
            }            
            a = stoi(stk.back());
            stk.pop_back();
            b = stoi(stk.back());
            stk.pop_back();

            if(tk == "+"){
                stk.push_back(to_string(a+b));
            }else if (tk == "-")
            {
                stk.push_back(to_string(b-a));
            }else if (tk == "*")
            {
                stk.push_back(to_string(b*a));
            }else if (tk == "/")
            {
                stk.push_back(to_string(b/a));
            }
        }

        return stoi(stk.back());

    }
};
