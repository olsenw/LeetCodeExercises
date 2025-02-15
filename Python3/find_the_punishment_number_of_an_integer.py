# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer n, return the punishment number of n.

    The punishment number of n is defined as the sum of the squares of all
    integers i such that:
    * 1 <= i <= n
    * The decimal representation of i * i can be partitioned into contiguous
      substrings such that the sum of the integer values of these substrings
      equals i.
    '''
    # hints helped
    def punishmentNumber(self, n: int) -> int:
        def test(target, partition):
            if target == 0 and (partition == '' or int(partition) == 0):
                return True
            for i in range(1, len(partition)+1):
                x = int(partition[:i])
                if x > target:
                    break
                if test(target - x, partition[i:]):
                    return True
            return False
        answer = 0
        for i in range(1, n+1):
            if test(i, str(i*i)):
                answer += i * i
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 10
        o = 182
        self.assertEqual(s.punishmentNumber(i), o)

    def test_two(self):
        s = Solution()
        i = 37
        o = 1478
        self.assertEqual(s.punishmentNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)