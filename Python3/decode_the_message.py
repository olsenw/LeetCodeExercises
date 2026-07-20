# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given the strings key and message, which represent a cipher key and a secret
    message, respectively. The steps to decode message are as follows:
    1. Use the first appearance of all 26 lowercase English letters in key as
       the order of the substitution table.
    2. Align the substitution table with the regular English alphabet.
    3. Each letter in message is then substituted using the table.
    4. Spaces ' ' are transformed to themselves.

    Return the decoded message.
    '''
    def decodeMessage(self, key: str, message: str) -> str:
        d = {' ':' '}
        m = 'a'
        for c in key:
            if c not in d:
                d[c] = m
                m = chr(ord(m) + 1)
        pass
        return "".join(d[c] for c in message)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "the quick brown fox jumps over the lazy dog"
        j = "vkbs bs t suepuv"
        o = "this is a secret"
        self.assertEqual(s.decodeMessage(i,j), o)

    def test_two(self):
        s = Solution()
        i = "eljuxhpwnyrdgtqkviszcfmabo"
        j = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
        o = "the five boxing wizards jump quickly"
        self.assertEqual(s.decodeMessage(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)