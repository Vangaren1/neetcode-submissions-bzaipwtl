
class Solution
{
private:
    unordered_set<string> words;
    int n;
    vector<string> curr;
    vector<string> results;

public:
    vector<string> wordBreak(string s, vector<string> &wordDict)
    {
        n = s.size();
        for (auto &word : wordDict)
        {
            words.insert(word);
        }

        backtrack(0, s);

        return results;
    }

    void backtrack(int index, string s)
    {
        if (index == n)
        {
            string sentence;

            for (int i = 0; i < curr.size(); i++)
            {
                if (i > 0)
                {
                    sentence += " ";
                }

                sentence += curr[i];
            }
            results.push_back(sentence);
            return;
        }

        for (auto &word : words)
        {
            string tmp(s.substr(index, word.size()));
            if (word != tmp)
            {
                continue;
            }

            curr.push_back(word);
            backtrack(index + word.size(), s);
            curr.pop_back();
        }
    }
};