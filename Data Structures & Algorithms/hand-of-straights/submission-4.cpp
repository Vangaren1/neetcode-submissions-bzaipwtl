class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        int n = hand.size();
        if (n % groupSize != 0)
        {
            return false;
        }

        unordered_map<int, int> count;

        for (int card : hand)
        {
            count[card]++;
        }

        vector<int> keys;

        for (const auto &[card, count] : count)
        {
            keys.push_back(card);
        }
        sort(keys.begin(), keys.end());

        for (int cardVal : keys)
        {
            while (count[cardVal] > 0)
            {
                for (int x = cardVal; x < cardVal + groupSize; x++)
                {
                    if (count[x] == 0)
                    {
                        return false;
                    }
                    count[x]--;
                }
            }
        }
        return true;
    }
};
