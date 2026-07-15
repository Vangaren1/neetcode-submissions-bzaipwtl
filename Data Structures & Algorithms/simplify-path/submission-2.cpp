class Solution {
public:
    string simplifyPath(string path)
    {
        vector<string> paths = split(path, '/');
        vector<string> stk;

        for (auto &p : paths)
        {
            if (p.size() > 0)
            {
                if (p == ".")
                {
                    continue;
                }
                if (p == "..")
                {
                    if (!stk.empty())
                    {
                        stk.pop_back();
                    }
                }
                else
                {
                    stk.push_back(p);
                }
            }
        }
        string result = "";
        for (auto &s : stk)
        {
            result += "/" + s;
        }
        if (result.size() == 0)
        {
            return "/";
        }
        return result;
    }
    vector<string> split(const string &text, char delim)
    {
        vector<string> parts;
        stringstream s(text);
        string part;

        while (getline(s, part, delim))
        {
            parts.push_back(part);
        }
        return parts;
    }
};