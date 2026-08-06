# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A password is said to be strong if it satisfies all the following criteria:
    * It has a least 8 characters.
    * It contains at least one lowercase letter.
    * It contains at least one uppercase letter.
    * It contains at least one special character. The special characters are the
      characters in the following string "!@#$%^&*()-+".
    * It does not contain 2 of the same character in adjacent positions (ie
      "aab" violates this condition, but "aba" does not).
    
    Given a string password, return true if it is a strong password. Otherwise
    return false.
    '''
    def strongPasswordCheckerII(self, password: str) -> bool:
        u = False
        l = False
        d = False
        s = False
        last = ""
        for c in password:
            if c == last:
                return False
            last = c
            u |= c.isupper()
            l |= c.islower()
            d |= c.isdigit()
            s |= c in "!@#$%^&*()-+"
        return all([len(password) >= 8, u, l, d, s, last])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "IloveLe3tcode!"
        o = True
        self.assertEqual(s.strongPasswordCheckerII(i), o)

    def test_two(self):
        s = Solution()
        i = "Me+You--IsMyDream"
        o = False
        self.assertEqual(s.strongPasswordCheckerII(i), o)

    def test_three(self):
        s = Solution()
        i = "1aB!"
        o = False
        self.assertEqual(s.strongPasswordCheckerII(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)