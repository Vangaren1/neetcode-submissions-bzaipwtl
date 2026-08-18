class Solution {
public:
    
    string convertToTitle(int columnNumber)
    {
string letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        string results = "";
        int m = 0;
        while (columnNumber)
        {
            columnNumber--;
            m = columnNumber % 26;
            results += letters[m];
            columnNumber -= m;
            columnNumber = columnNumber / 26;
        }
        reverse(results.begin(), results.end());
        return results;
    }
};