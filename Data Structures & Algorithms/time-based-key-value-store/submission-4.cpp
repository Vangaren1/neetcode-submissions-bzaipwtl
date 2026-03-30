
class TimeMap
{
private:
    unordered_map<string, vector<pair<string, int>>> keymap;
    string binarySearch(vector<pair<string, int>> &pairs, int timestamp)
    {
        int left{0}, mid{-1}, tmp{-1};
        int right = pairs.size() - 1;

        string result = "";
        while (left <= right)
        {
            mid = left + (right - left) / 2;
            tmp = pairs[mid].second;

            if (tmp <= timestamp)
            {
                result = pairs[mid].first;
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }

        return result;
    }

public:
    TimeMap()
    {
    }

    void set(string key, string value, int timestamp)
    {
        keymap[key].push_back({value, timestamp});
    }

    string get(string key, int timestamp)
    {
        return binarySearch(keymap[key], timestamp);
    }
};
