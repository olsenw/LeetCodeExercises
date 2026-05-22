# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
"""
class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return

class Solution:
    '''
    Given a callable function f(x,y) with a hidden formula and a value z,
    reverse engineer the formula and return all positive integer pairs x and y
    where f(x,y) == z. The pairs can be returned in any order.

    While the exact formula is hidden, the function is monotonically increasing,
    ie:
    * f(x,y) < f(x+1,y)
    * f(x,y) < f(x,y+1)

    This function interface is defined like this:

        interface CustomFunction {
        public:
        // Returns some positive integer f(x, y) for two positive integers x and y based on a formula.
        int f(int x, int y);
        };
    
    The solution is judged as follows:
    * The judge has a list of 9 hidden implementations of CustomFunction, along
      with a way to generate an answer key of all valid pairs for a specific z.
    * The judge will receive two inputs a function_id (to determine which
      implementation to test code with), and the target z.
    * The judge will call the findSolution and compare the results with the
      answer key.
    * If the results match the answer key, the solution will be accepted.
    '''
    # brute force the answer
    # only works due to problem restriction 1 <= x,y <= 1000
    def findSolution_brute(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        answer = []
        for x in range(1,1001):
            for y in range(1,1001):
                if customfunction.f(x,y) == z:
                    answer.append([x,y])
        return answer
    
    # addition of a binary search after looking at some online solutions
    # I like the optional None trick when answer is not found
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        def binary(x:int) -> Optional[int]:
            left,right = 1, 1000
            while left <= right:
                y = (left + right) // 2
                a = customfunction.f(x,y)
                if a == z:
                    return y
                elif a < z:
                    left = y + 1
                else:
                    right = y - 1
            return None
        answer = []
        for x in range(1,1001):
            y = binary(x)
            if y is not None:
                answer.append([x,y])
        return answer

class UnitTesting(unittest.TestCase):
    # tested online due to custom function implementations
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)