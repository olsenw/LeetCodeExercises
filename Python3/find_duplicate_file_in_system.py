# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import defaultdict

class Solution:
    '''
    Given a list paths of directory info, including the directory path and all
    the files with contents in this directory, return all the duplicate files in
    the system in terms of their paths. The answer may be returned in any order.

    A group of duplicate files consists of at least two files that have the same
    content.

    A single directory info string in the input list has following format:
    
    "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

    It means there are n files (f1.txt, f2.txt ... fn.txt) with contents 
    (f1_content, f2_content ... fn_content) respectively in the directory
    "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, it means the
    directory is just the root directory.

    The output is a list of groups of duplicate file paths. For each group, it
    contains all the file paths of the files that have the same content. A file
    path is a string that has the following format:

    "directory_path/file_name.txt"
    '''
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content = defaultdict(list)
        for p in paths:
            files = p.split(' ')
            for f in files[1:]:
                c = f.find('(')
                content[f[c+1:-1]].append(f'{files[0]}/{f[:c]}')
        return [i for i in content.values() if len(i) > 1]

    '''
    There were a bunch of follow-up questions... but ignored them.
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
        o = [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
        self.assertEqual(s.findDuplicate(i), o)

    def test_two(self):
        s = Solution()
        i = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
        o = [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
        self.assertEqual(s.findDuplicate(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)