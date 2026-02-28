# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers memory1 and memory2 representing the available memory on
    in bits on two memory sticks. There is currently a faulty program running
    that consumes an increasing amount of memory every second.

    At the ith second (starting from 1), i bits of memory are allocated to the
    stick with more available memory (or from the first memory stick if both
    have the same available memory). If neither stick has at least i bits of
    available memory, the program crashes.

    Return an array containing [crashTime, memory1crash, memory2crash], where
    crashTime is the time (in seconds) when the program crashed and memory1crash
    and memory2crash are the available bits of memory in the first and second
    sticks respectively.
    '''
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i = 1
        a,b = 0,0
        while True:
            if memory1 - a >= memory2 - b:
                if a + i > memory1:
                    break
                a += i
            else:
                if b + i > memory2:
                    break
                b += i
            i += 1
        return [i,memory1-a,memory2-b]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = 2
        o = [3,1,0]
        self.assertEqual(s.memLeak(i,j), o)

    def test_two(self):
        s = Solution()
        i = 8
        j = 11
        o = [6,0,4]
        self.assertEqual(s.memLeak(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)