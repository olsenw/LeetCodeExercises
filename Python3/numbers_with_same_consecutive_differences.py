# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Return all non-negative integers of length n such that the absolute
    difference between every two consecutive digits is k.

    Note that every number in the answer must not have leading zeros.

    Answer may be returned in any order.
    '''
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        answer = [1,2,3,4,5,6,7,8,9]
        for d in range(0,n-1):
            # d = 10 ** d
            update = []
            for a in answer:
                # f = a // d % 10
                l = a % 10
                # if f - k > 0:
                #     update.append((f - k) * d * 10 + a)
                # if f + k < 10:
                #     update.append((f + k) * d * 10 + a)
                if l - k >= 0:
                    update.append(a * 10 + l - k)
                if k > 0 and l + k < 10:
                    update.append(a * 10 + l + k)
            # answer = sorted(update)
            answer = update
        # return sorted(answer)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = 7
        o = [181,292,707,818,929]
        self.assertEqual(s.numsSameConsecDiff(i,j), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = 1
        o = [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
        self.assertEqual(s.numsSameConsecDiff(i,j), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = 1
        o = [101,121,123,210,212,232,234,321,323,343,345,432,434,454,456,543,545,565,567,654,656,676,678,765,767,787,789,876,878,898,987,989]
        self.assertEqual(s.numsSameConsecDiff(i,j), o)

    def test_four(self):
        s = Solution()
        i = 9
        j = 4
        o = [151515151,151515159,151515951,151515959,151595151,151595159,151595951,151595959,159515151,159515159,159515951,159515959,159595151,159595159,159595951,159595959,262626262,373737373,404040404,404040484,404048404,404048484,404840404,404840484,404848404,404848484,484040404,484040484,484048404,484048484,484840404,484840484,484848404,484848484,515151515,515151595,515159515,515159595,515951515,515951595,515959515,515959595,595151515,595151595,595159515,595159595,595951515,595951595,595959515,595959595,626262626,737373737,840404040,840404048,840404840,840404848,840484040,840484048,840484840,840484848,848404040,848404048,848404840,848404848,848484040,848484048,848484840,848484848,951515151,951515159,951515951,951515959,951595151,951595159,951595951,951595959,959515151,959515159,959515951,959515959,959595151,959595159,959595951,959595959]
        self.assertEqual(s.numsSameConsecDiff(i,j), o)

    def test_five(self):
        s = Solution()
        i = 2
        j = 0
        o = [11,22,33,44,55,66,77,88,99]
        self.assertEqual(s.numsSameConsecDiff(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)