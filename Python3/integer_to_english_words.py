# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Convert a non-negative integer num to its English words representation.
    '''
    def numberToWords(self, num: int) -> str:
        def ones(num):
            return ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"][num]
        def tens(num):
            # a = {10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety"}
            a = {2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety"}
            if num < 20:
                return ones(num)
            d,m = divmod(num, 10)
            if m:
                return a[d] + " " + ones(m)
            return a[d]
        def hundred(num):
            if num < 100:
                return tens(num)
            d,m = divmod(num, 100)
            if m:
                return ones(d) + " Hundred " + tens(m)
            return ones(d) + " Hundred"
        if num == 0:
            return "Zero"
        s = 0
        suffix = ["", "Thousand", "Million", "Billion"]
        stack = []
        while num:
            d,m = divmod(num, 1000)
            if m:
                if s > 0:
                    stack.append(hundred(m) + " " + suffix[s])
                else:
                    stack.append(hundred(m))
            s += 1
            num = d
        return " ".join(s for s in stack[::-1] if s != "")

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 123
        o = "One Hundred Twenty Three"
        self.assertEqual(s.numberToWords(i), o)

    def test_two(self):
        s = Solution()
        i = 12345
        o = "Twelve Thousand Three Hundred Forty Five"
        self.assertEqual(s.numberToWords(i), o)

    def test_three(self):
        s = Solution()
        i = 0
        o = "Zero"
        self.assertEqual(s.numberToWords(i), o)

    def test_four(self):
        s = Solution()
        i = 1234567
        o = "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
        self.assertEqual(s.numberToWords(i), o)

    def test_five(self):
        s = Solution()
        i = 2147483647
        o = "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"
        self.assertEqual(s.numberToWords(i), o)

    def test_six(self):
        s = Solution()
        i = 1000010
        o = "One Million Ten"
        self.assertEqual(s.numberToWords(i), o)

    def test_seven(self):
        s = Solution()
        i = 100
        o = "One Hundred"
        self.assertEqual(s.numberToWords(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)