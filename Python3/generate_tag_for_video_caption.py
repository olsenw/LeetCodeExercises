# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string caption representing the caption for a video.

    The following actions must be performed in order to generate a valid tag for
    the video:
    1) Combine all words in the string into a single camelCase string prefixed
       with '#'. A camelCase string is one where the first letter of all words
       except the first one is capitalized. All characters after the first
       character in each word must be lowercase.
    2) Remove all characters that are not an English letter except the first
       '#'.
    3) Truncate the result to a maximum of 100 characters.

    Return the tag after performing the actions on caption.
    '''
    def generateTag(self, caption: str) -> str:
        caption = caption.split()
        if len(caption) == 0:
            return "#"
        answer = "#" + caption[0].lower()
        for c in caption[1:]:
            answer += c[0].upper() + c[1:].lower()
        return answer[:100]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "Leetcode daily streak achieved"
        o = "#leetcodeDailyStreakAchieved"
        self.assertEqual(s.generateTag(i), o)

    def test_two(self):
        s = Solution()
        i = "can I Go There"
        o = "#canIGoThere"
        self.assertEqual(s.generateTag(i), o)

    def test_three(self):
        s = Solution()
        i = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
        o = "#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
        self.assertEqual(s.generateTag(i), o)

    def test_four(self):
        s = Solution()
        i = "Leetcode dAily streak achieved"
        o = "#leetcodeDailyStreakAchieved"
        self.assertEqual(s.generateTag(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)