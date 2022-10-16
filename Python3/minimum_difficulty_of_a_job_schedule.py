# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Schedule a list of jobs in d days. Jobs are dependent (i.e To work on the
    ith job, all jobs previous must be finished).

    Every day at least one task musk be completed. The difficulty of a job
    schedule is the sum of difficulties of each day of the d days. The
    difficulty of a day is the maximum difficulty of a job done on that day.

    Given an integer array jobDifficulty and an integer d. The difficulty of the
    ith job is jobDifficulty[i].

    Return the minimum difficulty of a job schedule. If it is not possible to
    find a job schedule return -1.
    '''
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        @cache
        def dp(i,r):
            if i == len(jobDifficulty) - 1:
                return jobDifficulty[i]
            if r == 0:
                return max(jobDifficulty[i:])
            m = jobDifficulty[i]
            n = m + dp(i+1, r-1)
            for j in range(i+1, len(jobDifficulty) - r + 1):
                t = m + dp(j, r-1)
                n = min(n, t)
                m = max(m, jobDifficulty[j])
            return n
        return dp(0, d-1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [6,5,4,3,2,1]
        j = 2
        o = 7
        self.assertEqual(s.minDifficulty(i,j), o)

    def test_two(self):
        s = Solution()
        i = [9,9,9]
        j = 4
        o = -1
        self.assertEqual(s.minDifficulty(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1]
        j = 3
        o = 3
        self.assertEqual(s.minDifficulty(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,5,4,6,2,8]
        j = 3
        o = 14
        self.assertEqual(s.minDifficulty(i,j), o)

    def test_five(self):
        s = Solution()
        i = [536, 654, 960, 399, 248, 810, 540, 25, 374, 366, 707, 880, 650, 308, 55, 923, 101, 118, 197, 741, 752, 453, 370, 561, 80, 343, 792, 937, 967, 411, 577, 860, 264, 401, 193, 3, 623, 711, 816, 927, 523, 823, 960, 432, 62, 580, 377, 890, 443, 801, 474, 611, 86, 391, 581, 517, 864, 12, 561, 183, 897, 598, 658, 302, 939, 192, 543, 422, 809, 303, 422, 342, 532, 512, 329, 40, 1000, 266, 566, 551, 805, 363, 412, 9, 936, 319, 972, 42, 86, 337, 543, 305, 813, 674, 697, 68, 11, 960, 714, 400, 143, 493, 246, 141, 577, 897, 529, 401, 273, 832, 799, 48, 96, 473, 35, 859, 342, 63, 692, 194, 417, 451, 908, 359, 644, 712, 312, 936, 793, 62, 427, 272, 827, 128, 991, 873, 75, 50, 57, 487, 253, 636, 431, 324, 686, 615, 844, 964, 470, 346, 13, 244, 734, 215, 328, 916, 952, 31, 19, 393, 784, 73, 562, 257, 576, 510, 211, 280, 368, 67, 396, 746, 195, 660, 512, 49, 424, 496, 414, 766, 484, 709, 897, 38, 503, 721, 556, 798, 24, 818, 767, 777, 753, 446, 907, 79, 609, 915, 459, 289, 788, 162, 220, 755, 953, 644, 328, 834, 491, 704, 157, 686, 657, 477, 281, 753, 664, 36, 796, 826, 807, 420, 659, 616, 199, 572, 828, 208, 142, 891, 788, 759, 869, 991, 421, 661, 780, 238, 998, 742, 888, 196, 314, 524, 915, 438, 472, 652, 357, 289, 337, 61, 68, 657, 689, 257, 536, 390, 700, 819, 358, 938, 357, 986, 199, 779, 858, 546, 494, 368, 360, 584, 778, 840, 736, 889, 193, 714, 863, 147, 612, 453, 642, 40, 874, 10, 858, 18, 619, 399, 410, 227, 140, 556, 469, 685, 58, 370, 546, 589]
        j = 6
        o = 2650
        self.assertEqual(s.minDifficulty(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)