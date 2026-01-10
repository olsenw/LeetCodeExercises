# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a fixed length integer array arr, duplicating each occurrence of zero,
    shifting the remaining elements to the right.

    Note that elements beyond the length of the original array are not written.
    Do the above modifications to the input array in place and do not return
    anything.
    '''
    # cheese answer
    # does not perform the operation in place
    def duplicateZeros_cheese(self, arr: List[int]) -> None:
        a = []
        for n in arr:
            if len(a) > len(arr):
                break
            if n == 0:
                a.append(0)
            a.append(n)
        for i in range(len(arr)):
            arr[i] = a[i]
        return

    # in place operation
    def duplicateZeros(self, arr: List[int]) -> None:
        j = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                j += 2
            else:
                j += 1
            if j >= len(arr):
                j -= 1
                break
        pass
        if j == len(arr):
            j -= 1
            if arr[i] == 0:
                arr[j] = 0
                i -= 1
                j -= 1
        for i in range(i, -1, -1):
            arr[j] = arr[i]
            if arr[j] == 0:
                arr[j-1] = 0
                j -= 1
            j -= 1
        return

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,0,2,3,0,4,5,0]
        o = [1,0,0,2,3,0,0,4]
        s.duplicateZeros(i)
        self.assertEqual(i, o)

    def test_two(self):
        s = Solution()
        i = [1,2,3]
        o = [1,2,3]
        s.duplicateZeros(i)
        self.assertEqual(i, o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,0]
        o = [1,2,3,0]
        s.duplicateZeros(i)
        self.assertEqual(i, o)

    def test_four(self):
        s = Solution()
        i = [1,2,3,0,0]
        o = [1,2,3,0,0]
        s.duplicateZeros(i)
        self.assertEqual(i, o)

    def test_five(self):
        s = Solution()
        i = [1,2,3,0,0,0]
        o = [1,2,3,0,0,0]
        s.duplicateZeros(i)
        self.assertEqual(i, o)

    def test_six(self):
        s = Solution()
        i = [1,0,2,3,0,0,0]
        o = [1,0,0,2,3,0,0]
        s.duplicateZeros(i)
        self.assertEqual(i, o)

    def test_seven(self):
        s = Solution()
        i = [1,2,3,0,5]
        o = [1,2,3,0,0]
        s.duplicateZeros(i)
        self.assertEqual(i, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)