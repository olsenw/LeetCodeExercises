# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Due to a bug, there are many duplicate folders in a file system. Given a 2D
    array paths, where paths[i] is an array representing an absolute path to the
    ith folder in the system.

    Two folders (not necessarily on the same level) are identical if they
    contain the same non-empty set of identical subfolders if they contain and
    underlying subfolder structure. The folders do not need to be at the root
    level to be identical. If two or more folders are identical, then mark the
    folders as well as their subfolders.

    Once all the identical folders and their subfolders have been marked, the
    file system will delete all of them. The file system only runs the deletion
    once, so any folders that become identical after the initial deletion are
    not deleted.

    Return the 2D array ans containing the paths of the remaining folder after
    deleting all the marked folders. The paths may be returned in any order.
    '''
    # deep dive into python class methods that does nothing
    def deleteDuplicateFolder_fails(self, paths: List[List[str]]) -> List[List[str]]:
        class Trie(object):
            def __init__(self):
                self.trie: Dict[str, Trie] = dict()
                self.path = False
            def __repr__(self):
                return f'Trie {self.trie} {self.path})'
            def __contains__(self, item:str):
                return item in self.trie
            def __setitem__(self, key:str, value):
                self.trie[key] = value
            def __getitem__(self, key:str):
                return self.trie[key]
            def __iter__(self):
                return iter(self.trie)
            def __eq__(self, other):
                if isinstance(other, Trie):
                    return self.path == other.path and self.trie == other.trie
                return False
            def __hash__(self):
                return hash((self.path, tuple((k,hash(self.trie[k])) for k in sorted(self.trie))))
            def add(self, path: List[str]):
                curr = self.trie
                for p in path:
                    if p not in curr:
                        curr[p] = Trie()
                    curr = curr[p]
                curr.path = True
        trie = Trie()
        for path in paths:
            trie.add(path)
        c = Counter()
        def dfs(trie:Trie):
            for i in trie:
                dfs(trie[i])
            c[trie] += 1
        dfs(trie)
        return

    def deleteDuplicateFolder_giveup(self, paths: List[List[str]]) -> List[List[str]]:
        class Trie:
            def __init__(self):
                self.trie: Dict[str, Trie] = dict()
                self.path = False
                self.delete = False
            def add(self, path:List[str]):
                curr = self
                for p in path:
                    if p not in curr.trie:
                        curr.trie[p] = Trie()
                    curr = curr.trie[p]
                curr.path = True
        trie = Trie()
        for path in paths:
            trie.add(path)
        c = Counter()
        def dfs(node: Trie):
            l = []
            for n in sorted(node.trie):
                pass
                l.append(dfs(node.trie[n]))
            h = hash(tuple(l))
            c[h] += 1
            return h
            return hash(tuple(dfs(node.trie[n]) for n in node.trie))
        dfs(trie)
        return

    # based on leetcode editorial
    # https://leetcode.com/problems/delete-duplicate-folders-in-system/editorial/?envType=daily-question&envId=2025-07-20
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        class Trie:
            # current nodes serialized representation
            serial: str = ""
            children: dict
            def __init__(self):
                self.children = dict()
        root = Trie()
        for path in paths:
            curr = root
            for p in path:
                if p not in curr.children:
                    curr.children[p] = Trie()
                curr = curr.children[p]
        # hash table recording number of times a serialized representation is encountered
        freq = Counter()
        # post order traversal to find serialized representations
        def construct(node: Trie):
            # leaf node, serialization is an empty string (default in Trie)
            if not node.children:
                return
            # track all serialized paths
            v = []
            # pre annotate variables used in for in loop
            folder:str
            child:Trie
            for folder, child in node.children.items():
                construct(child)
                v.append(f'{folder}({child.serial})')
            # enforce order
            v.sort()
            node.serial = "".join(v)
            freq[node.serial] += 1
        construct(root)
        # find all valid paths that serialization appears once
        answer = list()
        # stack to track current path
        path = list()
        def operate(node: Trie):
            # if serialization appears more than once skip ("delete")
            if freq[node.serial] > 1:
                return
            # ensure something in path (ie not at root)
            if path:
                answer.append(path[:])
            folder:str
            child:Trie
            for folder, child in node.children.items():
                path.append(folder)
                operate(child)
                path.pop()
        operate(root)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
        o = [["d"],["d","a"]]
        self.assertEqual(sorted(s.deleteDuplicateFolder(i)), sorted(o))

    def test_two(self):
        s = Solution()
        i = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
        o = [["c"],["c","b"],["a"],["a","b"]]
        self.assertEqual(sorted(s.deleteDuplicateFolder(i)), sorted(o))

    def test_three(self):
        s = Solution()
        i = [["a","b"],["c","d"],["c"],["a"]]
        o = [["c"],["c","d"],["a"],["a","b"]]
        self.assertEqual(sorted(s.deleteDuplicateFolder(i)), sorted(o))

if __name__ == '__main__':
    unittest.main(verbosity=2)