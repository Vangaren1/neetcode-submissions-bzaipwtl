class Solution
{
public:
    string encode(vector<string> &strs)
    {
        string result = "";
        for (string str : strs)
        {
            result += innerEncode(str) + '/';
        }
        return result;
    }

    string innerEncode(const string &str)
    {
        string result = "";
        char buffer[4];
        for (unsigned char ch : str)
        {
            sprintf(buffer, "%02XX", (unsigned int)ch);
            result += buffer;
        }
        return result;
    }

    string innerDecode(string s)
    {
        string result, curr;

        for (char c : s)
        {
            if (c == 'X')
            {
                result += static_cast<unsigned char>(stoi(curr, nullptr, 16));
                curr.clear();
            }
            else
            {
                curr += c;
            }
        }
        return result;
    }

    vector<string> decode(string s)
    {
        vector<string> result;
        string curr;

        for (char c : s)
        {
            if (c == '/')
            {
                result.push_back(innerDecode(curr));
                curr.clear();
            }
            else
            {
                curr += c;
            }
        }


        if (curr.size() > 0)
        {
            result.push_back(curr);
        }
        return result;
    }
};
