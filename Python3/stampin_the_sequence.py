# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

import heapq
from collections import deque

class Solution:
    '''
    Given two strings stamp and target. Initially, there is a string s
    of length target.length with all s[i] == '?'.

    In one turn, a stamp may placed over s and replace every letter in s
    with the corresponding letter from stamp.

    Note that stamp must be fully contained in the boundaries of s in
    order to stamp.

    Convert s to target using at most 10 * target.length turns.

    Return an array of the index of the left-most letter being stamped
    at each turn. If the target cannot be obtained from s within
    10 * target.length turns return an empty array.
    '''
    # fails... does not check proper stamp order
    def movesToStamp_fails(self, stamp: str, target: str) -> List[int]:
        heap = []
        for i in range(len(stamp)):
            if target[i] not in stamp[:i+1]:
                return []
        for i in range(len(target)):
            if i + len(stamp) - 1  == len(target):
                break
            m = sum(1 for a,b in zip(stamp, target[i:]) if a == b)
            if m:
                heapq.heappush(heap, (m,i))
        return [heapq.heappop(heap)[1] for _ in range(len(heap))]

    # based on leetcode solution
    # https://leetcode.com/problems/stamping-the-sequence/solution/
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        t, s = len(target), len(stamp)
        q = deque()
        complete = [False] * t
        changes = []
        answer = []
        for i in range(t - s + 1):
            # for window [i,i+s)
            # changes[i] contains info on steps before undo stamp
            made, todo = set(), set()
            for j,c in enumerate(stamp):
                a = target[i+j]
                if a == c:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            changes.append([made,todo])
            # if stamp can be immediately undone
            # enqueue letters from window
            if not todo:
                answer.append(i)
                for j in range(i,i+len(stamp)):
                    if not complete[j]:
                        q.append(j)
                        complete[j] = True
        # for each enqueued letter
        while q:
            i = q.popleft()
            # check each possible window
            for j in range(max(0,i-s+1), min(t-s, i)+1):
                # affected window
                if i in changes[j][1]:
                    # remove from todo
                    changes[j][1].discard(i)
                    # if todo is empty undo stamp
                    if not changes[j][1]:
                        answer.append(j)
                        # possible enqueued letters
                        for m in changes[j][0]:
                            if not complete[m]:
                                q.append(m)
                                complete[m] = True
        return answer[::-1] if all(complete) else []

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abc"
        j = "ababc"
        o = [1,0,2]
        self.assertEqual(s.movesToStamp(i,j), o)

    def test_two(self):
        s = Solution()
        i = "abca"
        j = "aabcaca"
        o = [2,3,0,1]
        self.assertEqual(s.movesToStamp(i,j), o)

    def test_three(self):
        s = Solution()
        i = "aye"
        j = "eyeye"
        o = []
        self.assertEqual(s.movesToStamp(i,j), o)

    def test_four(self):
        s = Solution()
        i = "cab"
        j = "cabbb"
        o = [2,1,0]
        self.assertEqual(s.movesToStamp(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)