# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a phone number as a string number. number consists of digits, spaces,
    and/or dashes.

    Reformat the phone number in a specific manner. Firstly, remove all spaces
    and dashes. Then, group the digits from left to right into blocks of length
    3 until there are 4 or fewer digits. The final digits are grouped as
    follows:
    * 2 digits: A single block of length 2.
    * 3 digits: A single block of length 3.
    * 4 digits: Two blocks of length 2 each.

    The blocks are then joined by dashes. Notice that the reformatting process
    should never produce any blocks of length 1 and produce at most two blocks
    of length 2.

    Return the phone number after formatting.
    '''
    def reformatNumber(self, number: str) -> str:
        answer = []
        hold = []
        for n in number:
            if n not in " -":
                hold.append(n)
                if len(hold) == 5:
                    answer.append("".join(hold[:3]))
                    hold = hold[3:]
        if len(hold) == 4:
            answer.append("".join(hold[:2]))
            answer.append("".join(hold[2:]))
        else:
            answer.append("".join(hold))
        return '-'.join(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1-23-45 6"
        o = "123-456"
        self.assertEqual(s.reformatNumber(i), o)

    def test_two(self):
        s = Solution()
        i = "123 4-567"
        o = "123-45-67"
        self.assertEqual(s.reformatNumber(i), o)

    def test_three(self):
        s = Solution()
        i = "123 4-5678"
        o = "123-456-78"
        self.assertEqual(s.reformatNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)