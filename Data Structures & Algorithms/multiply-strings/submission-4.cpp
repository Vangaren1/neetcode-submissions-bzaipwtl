class Solution {
public:
    string multiply(string num1, string num2) {
                // make sure that num1 is shorter than num2
        if (num1.size() > num2.size())
        {
            swap(num1, num2);
        }

        if(num1 == "0"){
            return "0";
        }

        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());

        vector<int> result;
        int carry = 0;
        for (int i = 0; i < num1.size(); i++)
        {
            int n1 = (int)(num1[i] - '0');
            carry = 0;
            for (int j = 0; j < num2.size(); j++)
            {
                if (i + j +1> result.size())
                {
                    result.push_back(0);
                }
                int n2 = (int)(num2[j] - '0');
                int prod = n1 * n2;
                int curr = result[i+j] + carry + prod;
                result[i + j] = curr % 10;
                carry = curr / 10;
            }
            if(carry){
                result.push_back(carry);
            }
        }
        reverse(result.begin(), result.end());

        string s = "";
        for (int k : result)
        {
            s = s + (char)(k + '0');
        }
        return s;
    }
};