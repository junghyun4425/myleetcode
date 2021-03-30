# Problem Link: https://leetcode.com/problems/design-twitter/

'''
문제 요약: 간단한 형태의 트위터를 구현하는 문제. (팔로우, 언팔로우, 포스팅, 최신 게시물 목록 등의 함수)
ask:
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
answer:
[null, null, [5], null, null, [6, 5], null, [5]]

해석:
생각보다 재밌게 해결했던 문제.
follower와 post 관리를 해쉬맵으로 하고, post는 안에 리스트로 구성, follower는 set으로 구성함.
가장 어려웠던 부분은 최근 게시물 10개를 나열하는 것인데, 시간데이터가 있으면 쉽지만 없으면 굉장히 골치아파짐.
고민끝에 임의의 시간데이터를 넣어줬고, 시간에 따라 정렬해 10개를 보여주는 방식으로 구현함.
시간복잡도, 공간복잡도 둘 모두 최상위권의 결과를 가짐.
'''

class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.posts = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.posts[userId].append((self.time, tweetId))
        self.followers[userId].add(userId)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        total = []
        for f in self.followers[userId]:
            total.extend(self.posts[f])
        total = [post for t, post in sorted(total, reverse=True)]
        if len(total) < 10:
            return total
        return total[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.followers[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)