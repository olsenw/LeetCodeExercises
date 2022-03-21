# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s. Partition the string into as many parts as
    possible so that each letter appears in at most one part.

    Note that the partition is done so that after concatenating all the
    parts in order, the resultanting string should be s.

    Return a list of integers representing the size of these parts.
    '''
    def partitionLabels(self, s: str) -> List[int]:
        # key char -> [first, last]
        d = dict()
        for i,c in enumerate(s):
            if c in d:
                d[c][1] = i
            else:
                d[c] = [i,i]
        # partition
        part = []
        i = 0
        while i < len(s):
            start, last = d[s[i]]
            for c in d:
                f, e = d[c]
                if start < f < last and last < e:
                    last = e
            i = last + 1
            part.append(last-start+1)
        return part

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "ababcbacadefegdehijhklij"
        o = [9,7,8]
        self.assertEqual(s.partitionLabels(i), o)

    def test_two(self):
        s = Solution()
        i = "eccbbbbdec"
        o = [10]
        self.assertEqual(s.partitionLabels(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)