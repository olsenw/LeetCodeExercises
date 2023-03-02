# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of characters chars, compress it using the following
    algorithm.

    Begin with an empty string s. For each group of consecutive repeating
    characters in chars:
    * If the groups length is 1, append the character to s.
    * Otherwise, append the character followed by the groups length.

    The compressed string s should not be returned separately, but instead, be
    stored in the input character array chars. Note that the group lengths that
    are 10 or longer will be split into multiple characters in chars.

    After modifying the input array return the new length of the array.

    Use constant extra space.
    '''
    def compress(self, chars: List[str]) -> int:
        last = chars[0]
        num = 1
        j = 0
        for i in range(1, len(chars)):
            if chars[i] != last:
                chars[j] = last
                j += 1
                if num > 1:
                    for d in str(num):
                        chars[j] = d
                        j += 1
                last = chars[i]
                num = 1
            else:
                num += 1
        chars[j] = last
        j += 1
        if num > 1:
            for d in str(num):
                chars[j] = d
                j += 1
        return j

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["a","a","b","b","c","c","c"]
        o = 6
        self.assertEqual(s.compress(i), o)
        self.assertEqual(i[:o], ["a","2","b","2","c","3"])

    def test_two(self):
        s = Solution()
        i = ["a"]
        o = 1
        self.assertEqual(s.compress(i), o)
        self.assertEqual(i[:o], ["a"])

    def test_three(self):
        s = Solution()
        i = ["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","b","b","c"]
        o = 6
        self.assertEqual(s.compress(i), o)
        self.assertEqual(i[:o], ["a","1","6","b","2","c"])

    def test_four(self):
        s = Solution()
        i = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        o = 4
        self.assertEqual(s.compress(i), o)
        self.assertEqual(i[:o], ["a","b","1","2"])

if __name__ == '__main__':
    unittest.main(verbosity=2)