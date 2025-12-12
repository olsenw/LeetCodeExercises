# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer numberOFUsers representing the total number of users and an
    array events of size n x 3.

    Each events[i] can be either of the following two types:
    1. Message Event: ["MESSAGE", "timestampi", "mentions_stringi]
      * This event indicates that a set of users was mentioned in a message at
        timestampi.
      * The mentions_stringi string can contain one of the following tokens:
        * id<number>: where <number> is an integer in range
          [0, numberOfUsers - 1]. There can be multiple ids separated by a
          single whitespace and may contain duplicates. This can mention even
          the offline users.
        * ALL: mentions all users.
        * HERE: mentions all online users.
    2. Offline Event: ["OFFLINE", "timestampi", "idi"]
        * This event indicates that the user idi had become offline at
          timestampi for 60 time units. The user will automatically be online
          again at time timestampi + 60.
        
    Return an array mentions where mentions[i] represents the number of mentions
    the user with id i has across all MESSAGE events.

    All users are initially online, and if a user goes offline or comes back
    online, their status change is processed before handling any message event
    that occurs at the same timestamp.

    Note that a user can be mentioned multiple times in a single message event,
    and each mention should be counted separately.
    '''
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x:(int(x[1]),x[0] != 'OFFLINE'))
        mentions = [0] * numberOfUsers
        online = [0] * numberOfUsers
        for type, time, data in events:
            time = int(time)
            if type[0] == "M":
                # all
                if data[0] == 'A':
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                # here
                elif data[0] == 'H':
                    for i in range(numberOfUsers):
                        if time >= online[i]:
                            mentions[i] += 1
                # mentions
                else:
                    for id in data.split():
                        mentions[int(id[2:])] += 1
            else:
                online[int(data)] = time + 60
        return mentions

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]
        o = [2,2]
        self.assertEqual(s.countMentions(i,j), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]
        o = [2,2]
        self.assertEqual(s.countMentions(i,j), o)

    def test_three(self):
        s = Solution()
        i = 2
        j = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]
        o = [0,1]
        self.assertEqual(s.countMentions(i,j), o)

    def test_four(self):
        s = Solution()
        i = 3
        j = [["MESSAGE","2","HERE"],["OFFLINE","2","1"],["OFFLINE","1","0"],["MESSAGE","61","HERE"]]
        o = [1,0,2]
        self.assertEqual(s.countMentions(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)