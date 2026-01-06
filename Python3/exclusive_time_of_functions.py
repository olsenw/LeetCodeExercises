# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    On a single-threaded CPU, a program with n functions is executed. Each
    function has a unique ID between 0 and n - 1.

    Function calls are stored in a call stack: when a function call starts, its
    ID is pushed onto the stack, and when a function call ends, its ID is popped
    off the stack. The function whose ID is at the top of the stack is the
    current function being executed. Each time a function starts or ends, it is
    written to the log with the IT, whether is started or ended, and the
    timestamp.

    Given a list logs, where logs[i] represents the ith log message formatted as
    a string "{function_id}:{start | end}:{timestamp}". Note that functions can
    be called multiple times, possibly recursively.

    A function's exclusive time is the sum of execution times for all function
    calls in the program.

    Return the exclusive time of each function in an array, where the value at
    the ith index represents the exclusive time for the function with ID i.
    '''
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        answer = [0] * (n+1)
        stack = [[-1,0]]
        for l in logs:
            l = l.split(':')
            id = int(l[0])
            start = l[1] == "start"
            time = int(l[2])
            if start:
                x,y = stack[-1]
                answer[x] += time - y
                stack.append([id,time])
            else:
                x,y = stack.pop()
                answer[x] += time - y + 1
                stack[-1][1] = time + 1
        return answer[:-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = ["0:start:0","1:start:2","1:end:5","0:end:6"]
        o = [3,4]
        self.assertEqual(s.exclusiveTime(i,j), o)

    def test_two(self):
        s = Solution()
        i = 1
        j = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
        o = [8]
        self.assertEqual(s.exclusiveTime(i,j), o)

    def test_three(self):
        s = Solution()
        i = 2
        j = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
        o = [7,1]
        self.assertEqual(s.exclusiveTime(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)