class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int ptr = digits.size() - 1;
        bool carry = true;
        while (ptr >= 0)
        {
            if (carry)
            {
                digits[ptr]++;
                carry = false;
            }
            if (digits[ptr] == 10)
            {
                digits[ptr] = 0;
                carry = true;
            }
            ptr--;
        }
        if (carry && digits.size() > 0)
        {
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};
