# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two binary strings a and b return their sum as a binary 
    string.
    '''
    def addBinary(self, a: str, b: str) -> str:
        from collections import deque
        da = deque(a)
        db = deque(b)
        carry = "0"
        ans = deque()
        while da or db:
            pa = da.pop() if da else "0"
            pb = db.pop() if db else "0"
            if pa == pb == "0":
                ans.appendleft(carry)
                carry = "0"
            elif pa == pb == "1":
                ans.appendleft(carry)
                carry = "1"
            else:
                if carry == "1":
                    ans.appendleft("0")
                else:
                    ans.appendleft("1")
        if carry == "1":
            ans.appendleft("1")
        return "".join(ans)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        a = "11"
        b = "1"
        o = "100"
        self.assertEqual(s.addBinary(a,b), o)

    def test_two(self):
        s = Solution()
        a = "1010"
        b = "1011"
        o = "10101"
        self.assertEqual(s.addBinary(a,b), o)

    def test_three(self):
        s = Solution()
        a = "1"
        b = "1000"
        o = "1001"
        self.assertEqual(s.addBinary(a,b), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)