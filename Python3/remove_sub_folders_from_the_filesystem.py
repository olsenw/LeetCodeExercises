# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a list of folders folder, return the folders after removing all
    sub-folders in those folders. The answer may be in any order.

    If a folder[i] is located withing another folder[j], it is called a
    sub-folder of it.

    The format of a path is one or more concatenated strings of the form '/'
    followed by one or more lowercase English letters.
    '''
    # /a/b/c will prevent /a/b/cd even though both are unique
    def removeSubfolders_wrong(self, folder: List[str]) -> List[str]:
        folder.sort()
        answer = [folder[0]]
        for i in range(len(folder)):
            if not folder[i].startswith(answer[-1]):
                answer.append(folder[i])
        return answer

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        def testing(a:str,b:str):
            a,b = a.split('/'), b.split('/')
            for i,j in zip(a,b):
                if i != j:
                    return True
            return False
        folder.sort()
        answer = [folder[0]]
        for f in folder[1:]:
            if testing(answer[-1], f):
                answer.append(f)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
        o = ["/a","/c/d","/c/f"]
        self.assertEqual(s.removeSubfolders(i), o)

    def test_two(self):
        s = Solution()
        i = ["/a","/a/b/c","/a/b/d"]
        o = ["/a"]
        self.assertEqual(s.removeSubfolders(i), o)

    def test_three(self):
        s = Solution()
        i = ["/a/b/c","/a/b/ca","/a/b/d"]
        o = ["/a/b/c","/a/b/ca","/a/b/d"]
        self.assertEqual(s.removeSubfolders(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)