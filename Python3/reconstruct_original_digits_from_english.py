# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s containing an out-of-order English representation of digits
    0-9, return the digits in ascending order.
    '''
    def originalDigits(self, s: str) -> str:
        # zero one two three four five six seven eight nine
        c = Counter(s)
        def deduct(word, times):
            for w in word:
                c[w] -= times
            return times
        a = [0] * 10
        # deduct unique words from the counter
        # Z - zero
        a[0] = deduct('zero', c['z'])
        # W - two
        a[2] = deduct('two', c['w'])
        # U - four
        a[4] = deduct('four', c['u'])
        # X - six
        a[6] = deduct('six', c['x'])
        # G - eight
        a[8] = deduct('eight', c['g'])
        # deduct non unique words
        # O - one
        a[1] = deduct('one', c['o'])
        # THR - three
        a[3] = deduct('three', c['t'])
        # F - five
        a[5] = deduct('five', c['f'])
        # S - seven
        a[7] = deduct('seven', c['s'])
        # deduct really non unique words
        # IE - nine
        a[9] = deduct('nine', c['i'])
        return "".join(str(i) * a[i] for i in range(10))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "owoztneoer"
        o = "012"
        self.assertEqual(s.originalDigits(i), o)

    def test_two(self):
        s = Solution()
        i = "fviefuro"
        o = "45"
        self.assertEqual(s.originalDigits(i), o)

    def test_three(self):
        s = Solution()
        i = ("zero" * 6) + ("one" * 3) + ("nine" * 24)
        o = ('0' * 6) + ('1' * 3) + ('9' * 24)
        self.assertEqual(s.originalDigits(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)