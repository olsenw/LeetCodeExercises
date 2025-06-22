# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A string s can be partitioned into groups of size k using the following
    procedure:
    * The first group consists of the first k characters of the string, the
      second group consists of the next k characters of the string, and so on.
      Each element can be a part of exactly one group.
    * For the last group, if the string does not have k character remaining, a
      character fill is used to complete the group.
    
    Note that the partition is done so that after removing the fill character
    from the last group (if it exists) and concatenating all the groups in
    order, the resultant string should be s.

    Given the string s, the size of each group k and the character fill, return
    a string array denoting the composition of every group s has been divided
    into, using the above procedure.
    '''
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        answer = []
        a = s[0]
        for i in range(1, len(s)):
            if i % k == 0:
                answer.append(a)
                a = ""
            a += s[i]
        for i in range(k - len(a)):
            a += fill
        answer.append(a)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcdefghi"
        j = 3
        k = "x"
        o = ["abc","def","ghi"]
        self.assertEqual(s.divideString(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = "abcdefghij"
        j  = 3
        k = "x"
        o = ["abc","def","ghi","jxx"]
        self.assertEqual(s.divideString(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)