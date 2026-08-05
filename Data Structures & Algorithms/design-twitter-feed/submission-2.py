class Twitter:

    def __init__(self):
        self.count = 0
        self.post = {}
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.post:
            self.post[userId] = []

        self.post[userId].append([self.count,tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = list(self.follows.get(userId, [])) + list([userId])

        feed = []

        for user in users:
            for tweet in self.post.get(user, []):
                heapq.heappush(feed, tweet)
        
        res = []

        while feed and len(res) < 10:
            res.append(heapq.heappop(feed)[1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId not in self.follows:
            self.follows[followerId] = set()

        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            return 

        self.follows[followerId].discard(followeeId)
