# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an array of positive integers arr, find a pattern of length m that is
    repeated k or more times.

    A pattern is a subarray (consecutive sub-sequence) that consists of one or
    more values, repeated multiple times consecutively without overlapping. A
    pattern is defined by its length and the number of repetitions.

    Return true if there exists a pattern of length m that is repeated k or more
    times, otherwise return false.
    '''
    # cannot turn arr into a string (values of arr can be more than 10)
    def containsPattern_fails(self, arr: List[int], m: int, k: int) -> bool:
        arr = "".join(str(i) for i in arr)
        freq = [arr[i:i+m] for i in range(len(arr) - m+1)]
        freq = Counter(freq)
        return any(freq[i] >= k for i in freq)

    # pattern needs to be consecutive (ie all together 123123)
    def containsPattern_fails(self, arr: List[int], m: int, k: int) -> bool:
        freq = Counter(["".join(str(c) for c in arr[i:i+m]) for i in range(len(arr)-m+1)])
        return any(freq[i] >= k for i in freq)

    # based on hint
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for a in range(len(arr) - m + 1):
            x = arr[a:a+m]
            for b in range(k):
                y = arr[a+(b*m):a+((b+1)*m)]
                if x != y:
                    break
            else:
                return True
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,4,4,4,4]
        j = 1
        k = 3
        o = True
        self.assertEqual(s.containsPattern(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1,2,1,2,1,1,1,3]
        j = 2
        k = 2
        o = True
        self.assertEqual(s.containsPattern(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [1,2,1,2,1,3]
        j = 2
        k = 3
        o = False
        self.assertEqual(s.containsPattern(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = [1,2,44,44,44,44]
        j = 1
        k = 3
        o = True
        self.assertEqual(s.containsPattern(i,j,k), o)

    def test_five(self):
        s = Solution()
        i = [2,2]
        j = 1
        k = 2
        o = True
        self.assertEqual(s.containsPattern(i,j,k), o)

    def test_six(self):
        s = Solution()
        i = [1,2,3,1,2]
        j = 2
        k = 2
        o = False
        self.assertEqual(s.containsPattern(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)