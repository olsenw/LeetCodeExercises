# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional, Tuple

'''
Design a simplified version of Twitter where users can post tweets,
follow/unfollow another user, and is able to see the 10 most recent tweets
in the user's news feed.

Implement the Twitter class:
'''
class Twitter:
    # maps a user id to a set of followed users
    follows = Dict[int, Set[int]]
    # maps a user id to a list of post id and an ordering
    posts = Dict[int, List[Tuple[int,int]]]
    # ordering number
    order: int

    '''
    Initializes the twitter object.
    '''
    def __init__(self):
        self.follows = dict()
        self.posts = dict()
        self.order = 0

    def _addUser(self, userId: int) -> None:
        if userId not in self.posts:
            self.follows[userId] = {userId}
            self.posts[userId] = list()

    '''
    Composes a new tweet with ID tweetId by the user userId. Each call to this
    function will be made with a unique tweetID.
    '''
    def postTweet(self, userId: int, tweetId: int) -> None:
        self._addUser(userId)
        self.posts[userId].append((tweetId, self.order))
        self.order += 1

    '''
    Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in
    the news feed must by posted by users who the user followed or by the user
    thyself. Tweets must be ordered from most recent to least recent.
    '''
    def getNewsFeed(self, userId: int) -> List[int]:
        self._addUser(userId)
        answer = []
        h = []
        for i in self.follows[userId]:
            j = len(self.posts[i]) - 1
            if j == -1:
                continue
            t,o = self.posts[i][j]
            heapq.heappush(h, (-o, t, i, j))
        while h and len(answer) < 10:
            _,t,i,j = heapq.heappop(h)
            answer.append(t)
            if j > 0:
                t,o = self.posts[i][j-1]
                heapq.heappush(h, (-o, t, i, j-1))
        return answer

    '''
    The user with ID followerId started following the user with ID followeeID
    '''
    def follow(self, followerId: int, followeeId: int) -> None:
        self._addUser(followerId)
        self._addUser(followeeId)
        self.follows[followerId].add(followeeId)

    '''
    The user with ID followerId started unfollowing the user wiht ID folleeId.
    '''
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._addUser(followerId)
        if followerId != followeeId:
            self.follows[followerId].discard(followeeId)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Twitter()
        s.postTweet(1, 5)
        self.assertEqual(s.getNewsFeed(1), [5])
        s.follow(1,2)
        s.postTweet(2,6)
        self.assertEqual(s.getNewsFeed(1), [6,5])
        s.unfollow(1,2)
        self.assertEqual(s.getNewsFeed(1), [5])

    def test_two(self):
        s = Twitter()
        s.postTweet(1, 1)
        self.assertEqual(s.getNewsFeed(1), [1])
        s.follow(2,1)
        self.assertEqual(s.getNewsFeed(2), [1])
        s.unfollow(2,1)
        self.assertEqual(s.getNewsFeed(2), [])

    def test_three(self):
        s = Twitter()
        s.follow(1,5)
        self.assertEqual(s.getNewsFeed(1), [])

if __name__ == '__main__':
    unittest.main(verbosity=2)