# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A newly designed keypad was tested, where a tester pressed a sequence of n
    keys, one at a time.

    Given a string keysPressed of length n, where keysPressed[i] was the ith key
    pressed in the testing sequence, and a sorted list releaseTimes, where
    releaseTime[i] was the time the ith key was released. Both arrays are
    0-indexed. The 0th key was pressed at the time 0, and every subsequent key
    was pressed at the exact time the previous key was released.

    The tester wants to know the key of the keypress that had the longest
    duration. The ith keypress had a duration of
    releaseTimes[i] - releaseTimes[i - 1], and the 0th keypress had a duration
    of releaseTimes[0].

    Note that the same key could have been pressed multiple times during the
    test, and these multiple presses of the same key may not have had the same
    duration.

    Return the key of the keypress that had the longest duration. If there are
    multiple such keypresses, return the lexicographically largest key of the
    keypresses.
    '''
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        return max((releaseTimes[0], keysPressed[0]), max((releaseTimes[i] - releaseTimes[i-1], keysPressed[i]) for i in range(1, len(keysPressed))))[1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [9,29,49,50]
        j = "cbcd"
        o = 'c'
        self.assertEqual(s.slowestKey(i,j), o)

    def test_two(self):
        s = Solution()
        i = [12,23,36,46,62]
        j = "spuda"
        o = 'a'
        self.assertEqual(s.slowestKey(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)