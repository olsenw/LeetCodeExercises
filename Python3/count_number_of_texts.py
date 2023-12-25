# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice is texting Bob using her phone. The mapping of digits to letters is
    shown in the figure below.

    In order to add a letter, Alice has to press the key of corresponding digit
    i times where i is the position of the letter in the key.
    * For example, to add the letter 's', Alice has to press '7' four times.
      Similarly, to add the letter 'k', Alice has to press '5' twice.
    * Note that the digits '0' and '1' do not map to any letters, so Alice does
      not use them.

    However, due to an error in transmission, Bob did not receive Alice's text
    message but received a string of pressed keys instead.
    * For example, when Alice sent the message "bob", Bob received the string
      "2266622".
    
    Given a string pressedKeys representing the string received by Bob, return
    the total number of possible text messages Alice could have sent.

    Since the answer may be very large, return it modulo 10^9 + 7.
    '''
    def countTexts_overcounts(self, pressedKeys: str) -> int:
        m = 10**9 + 7
        n = len(pressedKeys)
        dp = [0] * (n + 4)
        dp[-5] = 1
        for i in range(n-2,-1,-1):
            dp[i] = 1 + dp[i+1]
            if pressedKeys[i] == pressedKeys[i + 1]:
                dp[i] += 1 + dp[i+2]
                if i + 2 < n and pressedKeys[i] == pressedKeys[i + 2]:
                    dp[i] += 1 + dp[i + 3]
                    if i + 3 < n and pressedKeys[i] == pressedKeys[i + 3]:
                        dp[i] += 1 + dp[i + 4]
                        if i + 4 < n and pressedKeys[i] in "79" and pressedKeys[i] + pressedKeys[i + 4]:
                            dp[i] += 1 + dp[i + 5]
        return dp[0] % m

    # based on solution by vegishanmukh7
    # https://leetcode.com/problems/count-number-of-texts/solutions/2017753/simple-o-n-single-pass-solution/
    def countTexts(self, pressedKeys: str) -> int:
        m = 10**9 + 7
        n = len(pressedKeys)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i] = dp[i-1]
            if i - 2 >= 0 and pressedKeys[i-1] == pressedKeys[i-2]:
                dp[i] += dp[i-2]
                if i - 3 >= 0 and pressedKeys[i-1] == pressedKeys[i-3]:
                    dp[i] += dp[i-3]
                    if i - 4 >= 0 and pressedKeys[i-1] in "79" and pressedKeys[i-1] == pressedKeys[i-4]:
                        dp[i] += dp[i-4]
        return dp[-1] % m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "22233"
        o = 8
        self.assertEqual(s.countTexts(i), o)

    def test_two(self):
        s = Solution()
        i = "222222222222222222222222222222222222"
        o = 82876089
        self.assertEqual(s.countTexts(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)