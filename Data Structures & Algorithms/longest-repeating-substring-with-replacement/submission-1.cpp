class Solution
{
public:
    int characterReplacement(string s, int k)
    {
        unordered_map<char, int> charCount;
        priority_queue<pair<int, char>> freq;

        int maxLen{0}, currLen{0}, mostFreq{0}, left{0}, right{0};

        for (char ch : s)
        {
            charCount[ch]++;
            freq.push({charCount[ch], ch});

            currLen = right - left + 1;
            mostFreq = freq.top().first;
            while (currLen > (mostFreq + k))
            {

                charCount[s[left]]--;
                freq.push({charCount[s[left]], s[left]});
                left++;

                while (!freq.empty() && freq.top().first != charCount[freq.top().second])
                {
                    freq.pop();
                }

                currLen = right - left + 1;
                mostFreq = freq.top().first;
            }

            maxLen = max(maxLen, currLen);

            right++;
        }
        return maxLen;
    }
};
