# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n, return a string array answer (1-indexed) where:
    * answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    * answer[i] == "Fizz" if i is divisible by 3.
    * answer[i] == "Buzz" if i is divisible by 5.
    * answer[i] == i (as a string) if none of the above conditions are true.
    '''
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        o = ["1","2","Fizz"]
        self.assertEqual(s.fizzBuzz(i), o)

    def test_two(self):
        s = Solution()
        i = 5
        o = ["1","2","Fizz","4","Buzz"]
        self.assertEqual(s.fizzBuzz(i), o)

    def test_three(self):
        s = Solution()
        i = 15
        o = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
        self.assertEqual(s.fizzBuzz(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)