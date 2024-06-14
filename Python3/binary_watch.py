# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6
    LEDs on the bottom to represent the minutes (0-59). Each LED represents a 
    zero or one, with the least significant bit on the right.

    Given an integer turnedOn which represents the number of LEDs that are
    currently on (ignoring the PM), return all possible times the watch could
    represent. The answer may be in any order.

    The hour must not contain a leading zero.

    The minute must consist of two digits and may contain a leading zero.
    '''
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        h = defaultdict(list)
        for i in range(12):
            h[i.bit_count()].append(str(i))
        m = defaultdict(list)
        for j in range(60):
            m[j.bit_count()].append(f'{j:02d}')
        answer = []
        for i in range(min(turnedOn + 1, 4)):
            for x in h[i]:
                for y in m[turnedOn - i]:
                    answer.append(f'{x}:{y}')
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
        self.assertEqual(s.readBinaryWatch(i), o)

    def test_two(self):
        s = Solution()
        i = 9
        o = []
        self.assertEqual(s.readBinaryWatch(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)