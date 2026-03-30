class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].insert(0, (self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feedQ = []
        for twt in self.tweets.get(userId, []):
            heapq.heappush(feedQ, twt)
            if len(feedQ) > 10:
                heapq.heappop(feedQ)
        for follow in self.follows[userId]:
            f = self.tweets.get(follow) if follow != userId else []
            for feed in f:
                heapq.heappush(feedQ, feed)
                if len(feedQ) > 10:
                    heapq.heappop(feedQ)
        retList = heapq.nlargest(10, feedQ)
        return [i[1] for i in retList]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
