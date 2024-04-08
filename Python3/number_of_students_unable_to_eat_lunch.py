# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The school cafeteria offers circular and square sandwiches at lunch break,
    referred to by the numbers 0 and 1 respectively. All students stand in a
    queue. Each student either prefers square or circular sandwiches.

    The number of sandwiches in the cafeteria is equal to the number of
    students. The sandwiches are placed in a stack. At each step:
    * If the student at the front of the queue prefers the sandwich on the top
      of the stack, they will take it and leave the queue.
    * Otherwise, they will leave it and go to the queue's end.

    This continues until none of the queue students want to take the top
    sandwich and are thus unable to eat.

    Given two integer arrays students and sandwiches where sandwiches[i] is the
    type of the ith sandwich in the stack (i = 0 is the top of the stack) and
    students[j] is the preference of the jth student in the initial queue (j = 0
    is the front of the queue).

    Return the number of students that are unable to eat.
    '''
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(sandwiches)
        a,b = students.count(0), students.count(1)
        for i in range(n):
            if sandwiches[i] == 0:
                if a == 0:
                    return n - i
                a -= 1
            else:
                if b == 0:
                    return n - i
                b -= 1
        return 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,0,0]
        j = [0,1,0,1]
        o = 0
        self.assertEqual(s.countStudents(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,0,0,1]
        j = [1,0,0,0,1,1]
        o = 3
        self.assertEqual(s.countStudents(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)