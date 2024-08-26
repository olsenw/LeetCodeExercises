# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array digits, where each element is a digit. The array may
    contain duplicates.

    Find all the unique integers that follow the given requirements:
    * The integer consists of the concatenation of three elements from digits in
      any arbitrary order.
    * The integer does not have leading zeros.
    * The integer is even.

    For example, if the given digits were [1,2,3], integers 132 and 312 follow
    the requirements.

    Return a sorted array of the unique integers.
    '''
    # Leetcode hint very useful
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        answer = []
        digit = Counter(digits)
        for i in range(100, 999, 2):
            j = i
            a = Counter()
            while j:
                a[j % 10] += 1
                j //= 10
            if all(a[j] <= digit[j] for j in a):
                answer.append(i)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,3,0]
        o = [102,120,130,132,210,230,302,310,312,320]
        self.assertEqual(s.findEvenNumbers(i), o)

    def test_two(self):
        s = Solution()
        i = [2,2,8,8,2]
        o = [222,228,282,288,822,828,882]
        self.assertEqual(s.findEvenNumbers(i), o)

    def test_three(self):
        s = Solution()
        i = [3,7,5]
        o = []
        self.assertEqual(s.findEvenNumbers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)