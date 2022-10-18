# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    The count-and-say sequence is a sequence defined by the recursive formula:
    * countAndSay(1) = "1"
    * countAndSay(n) is the way you would "say" the digit string from
      countAndSay(n-1), which is then converted into a different digit string.
    
    To determine how to "say" a digit string, split it into the minimal number
    of substrings such that each substring contains exactly one unique digit.
    Then for each substring, say the number of digits, then say the digit.
    Finally concatenate every said digit.

    For example, the saying and conversion for the digit string "3322251":
    "3322251"
    two 3's, three 2's, one 5, and one 1
    2 3 + 3 2 + 1 5 + 1 1
    "23321511"

    Given a positive integer n, return the nth term of the count-and-say
    sequence.
    '''
    def countAndSay(self, n: int) -> str:
        a = "1"
        for _ in range(n-1):
            b = ""
            c = 1
            d = a[0]
            for i in a[1:]:
                if i == d:
                    c += 1
                else:
                    b += str(c) + d
                    c = 1
                    d = i
            a = b + str(c) + d
        return a
    
'''
Can brute force a solution by haveing all 30 possible cases in a lookup table.
'''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = "1"
        self.assertEqual(s.countAndSay(i), o)

    def test_two(self):
        s = Solution()
        i = 4
        o = "1211"
        self.assertEqual(s.countAndSay(i), o)

    def test_three(self):
        s = Solution()
        i = 23
        o = "111312211312111322212321121113121112131112132112311321322112111312212321121113122112131112131221121321132132211231131122211331121321232221121113122113121113222123112221221321132132211231131122211331121321232221123113112221131112311332111213122112311311123112112322211211131221131211132221232112111312211322111312211213211312111322211231131122111213122112311311221132211221121332211213211321322113311213212312311211131122211213211331121321123123211231131122211211131221131112311332211213211321223112111311222112132113213221123123211231132132211231131122211311123113322112111312211312111322212321121113122123211231131122113221123113221113122112132113213211121332212311322113212221"
        self.assertEqual(s.countAndSay(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)