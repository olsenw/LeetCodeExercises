# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of digits which is sorted in non-decreasing order.
    It is possible to write numbers using each digits[i] multiple times.
    For example, if digits[1,3,5], possible to write numbers such as 13
    551 and 1251315.

    Return the number of positive integers that can be generated that
    are less than or equal to a given integer n.
    '''
    # see comment under function for how it works (basically counting)
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # turn n into a string of characters (allows comparison with digits)
        s = str(n)
        # total number of digits in n (convenient to have as variable)
        k = len(s)
        # dynamic programing array (valid integers if given substring of n)
        # d[i] = total valid ints given n[i:]
        dp = [0] * k + [1]
        # populate dp array
        for i in range(k-1, -1, -1):
            for d in digits:
                if d < s[i]:
                    dp[i] += len(digits) ** (k-i-1)
                elif d == s[i]:
                    # safe because dp is one longer than s is
                    dp[i] += dp[i+1]
        # dp answer + all the sub answers that could be added
        # dp is k length choice, while sum is all k-x permutations
        return dp[0] + sum(len(digits) ** i for i in range(1, k))

    '''
    Counting Example (what algorithm is doing)
    k = length of n (ie n = 456 then k = 3)

    # sum up all permutations with repetition (n^r) for [1, k-1]
    solution += (number digits) ^ (1)
    solution += (number digits) ^ (1)
    solution += ...
    solution += (number digits) ^ (k-2)
    solution += (number digits) ^ (k-1)

    dp = array of length k + 1 initialized to zero
    dp[k] = 1 (last element in dp array is one instead of zero)
              [only needed when one digit can be in last position]

    # calculate the permutations for substrings of n
    if digits[0] less than n[k-1] then dp[k-1] += (number digits) ^ (k-(k-1)-1) 
    if digits[1] less than n[k-1] then dp[k-1] += (number digits) ^ (k-(k-1)-1) 
    ...
    if digits[x] less than n[k-1] then dp[k-1] += (number digits) ^ (k-(k-1)-1) 
    if digits[x] equal n[k-1] then dp[k-1] += dp[k] 

    if digits[0] less than n[k-2] then dp[k-2] += (number digits) ^ (k-(k-2)-1) 
    if digits[1] less than n[k-2] then dp[k-2] += (number digits) ^ (k-(k-2)-1) 
    ...
    if digits[x-1] less than n[k-2] then dp[k-2] += (number digits) ^ (k-(k-2)-1) 
    if digits[x] equal n[k-2] then dp[k-2] += dp[k-1] 

    ...

    if digits[0] less than n[0] then dp[0] += (number digits) ^ (k-(0)-1) 
    if digits[1] less than n[0] then dp[0] += (number digits) ^ (k-(0)-1) 
    ...
    if digits[x-1] less than n[0] then dp[0] += (number digits) ^ (k-(0)-1) 
    if digits[x] equal n[0] then dp[0] += dp[1] 

    soultion += dp[0]
    '''
    '''
    Counting example visually
    digits = [1,2,3] n = 131

    all allowed
    3^1 =>  '1' '2' '3'
        3 possible options

    all allowed
    3^2 =>  '11' '12' '13'
            '21' '22' '23'
            '31' '32' '33'
        9 possible options
    
    partially allowed (left of line yes, right of line no)
    (note how anything left of the line is computed in the subproblems)
                                                     |___________
    3^3 =>  '111' '112' '113' '121' '122' '123' '131'|'132' '133'
            -----------------------------------------|
            '211' '212' '213' '221' '222' '223' '231' '232' '233'
            etc

            (digit options) ^ (3-(3-1)-1) + subproblem(dp[1])
    
        so assuming '1' digit in first place can get

        '11' '12' '13'
        '21' '22' '23'
            |_________
        '31'|'32' '33'
        ----|

            (digit options) ^ (3-(2-1)-1) + subproblem(dp[2])
            (digit options) ^ (3-(2-1)-1) + subproblem(dp[2])
             + subproblem(dp[2])

        so assuming '1','2','3' in third place can get [BASE CASE]
           |______
        '1'|'2' '3'
        ----

           subproblem(dp[3])

        so doing the calculate the sub problems then can do the addition
        dp[0] = dp[1]
        dp[1] = (3^1) + (3^1) + dp[2]
        dp[2] = 1

        (((3)^1) + ((3)^1) + (1))
        (3 + 3 + 1)
        7

     '''

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        self.assertEqual(s.atMostNGivenDigitSet(["1","3","5","7"], n = 100), 20)

    def test_two(self):
        s = Solution()
        self.assertEqual(s.atMostNGivenDigitSet(["1","4","9"], n = 1000000000), 29523)

    def test_three(self):
        s = Solution()
        self.assertEqual(s.atMostNGivenDigitSet(["7"], n = 8), 1)

    def test_four(self):
        s = Solution()
        self.assertEqual(s.atMostNGivenDigitSet(["1","2","3"], n = 131), 19)

    def test_five(self):
        s = Solution()
        self.assertEqual(s.atMostNGivenDigitSet(["1","2"], n = 11), 3)

    def test_six(self):
        s = Solution()
        self.assertEqual(s.atMostNGivenDigitSet(["5","7","8"], n = 59), 6)

    def test_seven(self):
        s = Solution()
        self.assertEqual(s.atMostNGivenDigitSet(["3","4","5","6"], n = 64), 18)

    def test_eight(self):
        s = Solution()
        self.assertEqual(s.atMostNGivenDigitSet(["2","3","4","6","8"], n = 61), 20)

    def test_nine(self):
        s = Solution()
        self.assertEqual(s.atMostNGivenDigitSet(["1","7"], n = 231), 10)


if __name__ == '__main__':
    unittest.main(verbosity=2)