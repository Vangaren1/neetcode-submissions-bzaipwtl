class Solution
{
public:
    string decodeString(string s)
    {
        if (s.find('[') == string::npos)
        {
            return s;
        }

        int start = 0;

        while (start < s.size() &&
               !isdigit(static_cast<unsigned char>(s[start])))
        {
            start++;
        }

        int end = start;

        while (end < s.size() &&
               isdigit(static_cast<unsigned char>(s[end])))
        {
            end++;
        }

        string front = s.substr(0, start);

        // Characters from start up to, but not including, end
        int num = stoi(s.substr(start, end - start));

        // end points at '['
        int ptr = end + 1;
        int bracketCount = 1;

        while (bracketCount > 0)
        {
            if (s[ptr] == '[')
            {
                bracketCount++;
            }
            else if (s[ptr] == ']')
            {
                bracketCount--;
            }

            ptr++;
        }

        // ptr is now one position after the matching ']'
        string mid = s.substr(end + 1, ptr - end - 2);
        string back = s.substr(ptr);

        mid = decodeString(mid);
        back = decodeString(back);

        string result = front;

        for (int i = 0; i < num; i++)
        {
            result += mid;
        }

        result += back;

        return result;
    }
};