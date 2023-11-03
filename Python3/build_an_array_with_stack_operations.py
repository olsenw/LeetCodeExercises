# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array target and an integer n.

    Given an empty stack with the two following operations:
    * "Push": pushes an integer to the top of the stack.
    * "Pop": removes the integer on the top of the stack.

    Also given is a stream of integers in the range [1, n].

    Use the two stack operations to make the numbers in the stack (from the
    bottom to the top) equal to target. Obey the following rules:
    * If the stream of integers is not empty, pick the next integer from the
      stream and push it onto the top of the stack.
    * If the stack is not empty, pop the integer at the top of the stack.
    * If, at any moment, the elements in the stack (from the bottom to the top)
      are equal to target, do not read new integers from the stream and do not
      perform any further operations on the stack.
    
    Return the stack operations needed to build target following the mentioned
    rules. If there are multiple valid answers, return any of them.
    '''
    def buildArray_passes(self, target: List[int], n: int) -> List[str]:
        answer = []
        i = 1
        for t in target:
            pass
            while i < t:
                answer.append('Push')
                answer.append('Pop')
                i += 1
            answer.append('Push')
            i += 1
        return answer

    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer = ["Push", "Pop"] * (target[0] - 1)
        answer.append('Push')
        for i in range(1, len(target)):
            pass
            answer.extend(["Push", "Pop"] * (target[i] - target[i-1] - 1))
            answer.append("Push")
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3]
        j = 3
        o = ["Push","Push","Pop","Push"]
        self.assertEqual(s.buildArray(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3]
        j = 3
        o = ["Push","Push","Push"]
        self.assertEqual(s.buildArray(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2]
        j = 4
        o = ["Push","Push"]
        self.assertEqual(s.buildArray(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,3,4]
        j = 5
        o = ["Push","Push","Pop","Push","Push"]
        self.assertEqual(s.buildArray(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)