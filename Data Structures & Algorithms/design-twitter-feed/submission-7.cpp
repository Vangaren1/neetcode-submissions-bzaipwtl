class Twitter
{
private:
    unordered_map<int, unordered_set<int>> whofollows;
    unordered_map<int, vector<pair<int, int>>> tweets;
    int time;

    vector<pair<int, int>> getLast10(int userId)
    {
        int c = min(10, (int)tweets[userId].size());
        vector<pair<int, int>> last10(tweets[userId].end() - c, tweets[userId].end());
        return last10;
    }

public:
    Twitter()
    {
        time = 0;
    }

    void postTweet(int userId, int tweetId)
    {
        tweets[userId].push_back({time, tweetId});
        time++;
    }

    vector<int> getNewsFeed(int userId)
    {
        priority_queue<pair<int, int>> newsFeed;
        for (const auto &p : getLast10(userId))
        {
            newsFeed.push(p);
        }
        for (int followee : whofollows[userId])
        {
            if (followee != userId)
            {
                for (const auto &p : getLast10(followee))
                {
                    newsFeed.push(p);
                }
            }
        }
        vector<int> result;
        int c = min(10, (int)newsFeed.size());
        for (int i = 0; i < c; i++)
        {
            result.push_back(newsFeed.top().second);
            newsFeed.pop();
        }
        return result;
    }

    void follow(int followerId, int followeeId)
    {
        whofollows[followerId].insert(followeeId);
    }

    void unfollow(int followerId, int followeeId)
    {
        if (whofollows[followerId].count(followeeId))
        {
            whofollows[followerId].erase(followeeId);
        }
    }
};