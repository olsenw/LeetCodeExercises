# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string path, which is an absolute path (starting with a
    slash '/') to a file or directory in a Unix-style file system,
    convert it to the simplified canonical path.

    In a Unix-style file system, a period '.' refers to the current
    directory, a double period '..' refers to the directory up a level,
    and any multiple consecutive slashes '//' are treated as a single
    slash '/'. For this problem, any other format of periods such as 
    '...' are treated as file/directory names.

    The canonical path should have the following format:
    * The path starts with a single slash '/'.
    * Any two directories are seperated by a single slash '/'.
    * The path does not end with a trailing '/'.
    * The path only contains the directories on the path from the root
      directory to the target file or directory (ie no period or double
      period)

    Return the simplified canonical path.
    '''
    def simplifyPath(self, path: str) -> str:
        from collections import deque
        queue = deque()
        i = 0
        while i < len(path):
            token = ""
            # take characters until finished with current token
            while i < len(path) and path[i] != '/':
                token += path[i]
                i += 1
            # strip/skip '/'
            while i < len(path) and path[i] == '/':
                i += 1
            # check if token is current directory '.'
            if token == '.':
                continue
            # check if token is parent directory
            elif token == '..':
                if queue:
                    queue.pop()
                if not queue:
                    queue.append("")
                continue
            # push token onto stack
            else:
                queue.append(token)
        # traverse queue to create canonical path
        return '/'.join(queue) if len(queue) > 1 else '/'

    def simplifyPath_revised(self, path: str) -> str:
        from collections import deque
        queue = deque()
        i = 0
        # strip/skip leading '/'
        while i < len(path) and path[i] == '/':
            i += 1
        # collect tokens
        while i < len(path):
            token = ""
            # take characters until finished with current token
            while i < len(path) and path[i] != '/':
                token += path[i]
                i += 1
            # strip/skip '/'
            while i < len(path) and path[i] == '/':
                i += 1
            # check if token is current directory '.'
            if token == '.':
                continue
            # check if token is parent directory
            elif token == '..':
                if queue:
                    queue.pop()
                continue
            # push token onto stack
            else:
                queue.append(token)
        # traverse queue to create canonical path
        return '/' + '/'.join(queue)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "/home/"
        o = "/home"
        self.assertEqual(s.simplifyPath(i), o)
        self.assertEqual(s.simplifyPath_revised(i), o)

    def test_two(self):
        s = Solution()
        i = "/../"
        o = "/"
        self.assertEqual(s.simplifyPath(i), o)
        self.assertEqual(s.simplifyPath_revised(i), o)

    def test_three(self):
        s = Solution()
        i = "/home//foo/"
        o = "/home/foo"
        self.assertEqual(s.simplifyPath(i), o)
        self.assertEqual(s.simplifyPath_revised(i), o)

    def test_four(self):
        s = Solution()
        i = "/"
        o = "/"
        self.assertEqual(s.simplifyPath(i), o)
        self.assertEqual(s.simplifyPath_revised(i), o)

    def test_five(self):
        s = Solution()
        i = "/./././././home"
        o = "/home"
        self.assertEqual(s.simplifyPath(i), o)
        self.assertEqual(s.simplifyPath_revised(i), o)

    def test_six(self):
        s = Solution()
        i = "///../////.//.././../home"
        o = "/home"
        self.assertEqual(s.simplifyPath(i), o)
        self.assertEqual(s.simplifyPath_revised(i), o)

    def test_seven(self):
        s = Solution()
        i = "/foo/bar/../bar/.././.."
        o = "/"
        self.assertEqual(s.simplifyPath(i), o)
        self.assertEqual(s.simplifyPath_revised(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)