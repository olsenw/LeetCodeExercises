# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from tkinter.messagebox import RETRY
from turtle import st
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Set

class Solution:
    '''
    Given an m x n board of characters and a list of strings words, return all
    words on the board.

    Each word must be constructed from letters of sequentially adjacent cells,
    where adjacent calls are horizontally or vertically neighboring. The same
    letter cell may not be used more than once in a word.
    '''
    # O(m * n * 4^s) time [m is width board, n is height board, s is length string]
    # time limit exceeded (42 / 64 test cases)
    def findWords_brute_dfs(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        # preform a dfs search on the board to find word
        def dfs(w, i, j, k, s):
            # invalid case - failure
            if (i, j) in s or k == len(w) or board[i][j] != w[k]:
                return False
            # base case - success
            if k == len(w) - 1 and board[i][j] == w[k]:
                return True
            # prevent revisit
            s.add((i, j))
            # go up
            if i > 0 and dfs(w, i - 1, j, k + 1, s):
                return True
            # go down
            if i < m - 1 and dfs(w, i + 1, j, k + 1, s):
                return True
            # go left
            if j > 0 and dfs(w, i, j - 1, k + 1, s):
                return True
            # go right
            if j < n - 1 and dfs(w, i, j + 1, k + 1, s):
                return True
            # did not find the word
            s.remove((i,j))
            return False
        # perform dfs on all positions in board for word
        def find(w):
            for i in range(m):
                for j in range(n):
                    if dfs(w,i,j,0,set()):
                        return True
            return False
        # return only found words
        return [w for w in words if find(w)]

    class Trie:
        def __init__(self):
            self.words = []
            self.t = dict()

        def add(self, word):
            trie = self
            for w in word:
                if w not in trie.t:
                    trie.t[w] = Solution.Trie()
                trie = trie.t[w]
            trie.words.append(word)

    # time limit exceeded (38 / 64 test cases)
    def findWords_trie_dfs(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Solution.Trie()
        for w in words:
            trie.add(w)
        found = set()
        m, n = len(board), len(board[0])
        def dfs(i,j,s:Set,t:Solution.Trie):
            # failure - bail
            if (i,j) in s or board[i][j] not in t.t:
                return
            # success
            if board[i][j] in t.t and t.t[board[i][j]].words:
                found.update(t.t[board[i][j]].words)
            s.add((i,j))
            # up
            if i > 0:
                dfs(i - 1, j, s, t.t[board[i][j]])
            # down
            if i < m - 1:
                dfs(i + 1, j, s, t.t[board[i][j]])
            # left
            if j > 0:
                dfs(i, j - 1, s, t.t[board[i][j]])
            # right
            if j < n - 1:
                dfs(i, j + 1, s, t.t[board[i][j]])
            s.remove((i,j))
        for i in range(m):
            for j in range(n):
                dfs(i,j,set(), trie)
        return list(found)

    class TrieTwo:
        def __init__(self):
            self.word = None
            self.t = dict()

        def add(self, word):
            trie = self
            for w in word:
                if w not in trie.t:
                    trie.t[w] = Solution.TrieTwo()
                trie = trie.t[w]
            trie.word = word

        def remove(self, word):
            trie = self
            stack = []
            for w in word:
                if w not in trie.t:
                    return
                stack.append(trie)
                trie = trie.t[w]
            trie.word = None
            for w in word[::-1]:
                if stack[-1].t[w].word or stack[-1].t[w].t:
                    return
                del stack[-1].t[w]
                stack.pop()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie
        trie = Solution.TrieTwo()
        for w in words:
            trie.add(w)
        # size of board
        m, n = len(board), len(board[0])
        # words that have been found so far
        found = []
        # depth first search from a position (no reusing positions)
        def dfs(i, j, s:Set, t:Solution.TrieTwo):
            # failure - bail
            if (i,j) in s:
            # if (i,j) in s or board[i][j] not in t.t:
                return
            # success
            if board[i][j] in t.t and t.t[board[i][j]].word:
                found.append(t.t[board[i][j]].word)
                trie.remove(found[-1])
            s.add((i,j))
            # up
            if i > 0 and board[i][j] in t.t:
                dfs(i - 1, j, s, t.t[board[i][j]])
            # down
            if i < m - 1 and board[i][j] in t.t:
                dfs(i + 1, j, s, t.t[board[i][j]])
            # left
            if j > 0 and board[i][j] in t.t:
                dfs(i, j - 1, s, t.t[board[i][j]])
            # right
            if j < n - 1 and board[i][j] in t.t:
                dfs(i, j + 1, s, t.t[board[i][j]])
            s.remove((i,j))
        for i in range(m):
            for j in range(n):
                dfs(i, j, set(), trie)
        return found

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        j = ["oath","pea","eat","rain"]
        o = ["eat", "oath"]
        self.assertEqual(sorted(s.findWords(i,j)), o)

    def test_two(self):
        s = Solution()
        i = [["a","b"],["c","d"]]
        j = ["abcb"]
        o = []
        self.assertEqual(s.findWords(i,j), o)

    def test_three(self):
        s = Solution()
        i = [["a","a"]]
        j = ["aaa"]
        o = []
        self.assertEqual(s.findWords(i,j), o)

    def test_four(self):
        s = Solution()
        i = [["a"]]
        j = ["b","a"]
        o = ["a"]
        self.assertEqual(s.findWords(i,j), o)

    def test_five(self):
        s = Solution()
        i = [["a","a","a"]]
        j = ["b","a","aa"]
        o = ["a", "aa"]
        self.assertEqual(s.findWords(i,j), o)

    def test_six(self):
        s = Solution()
        i = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
        j = ["lllllll","fffffff","ssss","s","rr","xxxx","ttt","eee","ppppppp","iiiiiiiii","xxxxxxxxxx","pppppp","xxxxxx","yy","jj","ccc","zzz","ffffffff","r","mmmmmmmmm","tttttttt","mm","ttttt","qqqqqqqqqq","z","aaaaaaaa","nnnnnnnnn","v","g","ddddddd","eeeeeeeee","aaaaaaa","ee","n","kkkkkkkkk","ff","qq","vvvvv","kkkk","e","nnn","ooo","kkkkk","o","ooooooo","jjj","lll","ssssssss","mmmm","qqqqq","gggggg","rrrrrrrrrr","iiii","bbbbbbbbb","aaaaaa","hhhh","qqq","zzzzzzzzz","xxxxxxxxx","ww","iiiiiii","pp","vvvvvvvvvv","eeeee","nnnnnnn","nnnnnn","nn","nnnnnnnn","wwwwwwww","vvvvvvvv","fffffffff","aaa","p","ddd","ppppppppp","fffff","aaaaaaaaa","oooooooo","jjjj","xxx","zz","hhhhh","uuuuu","f","ddddddddd","zzzzzz","cccccc","kkkkkk","bbbbbbbb","hhhhhhhhhh","uuuuuuu","cccccccccc","jjjjj","gg","ppp","ccccccccc","rrrrrr","c","cccccccc","yyyyy","uuuu","jjjjjjjj","bb","hhh","l","u","yyyyyy","vvv","mmm","ffffff","eeeeeee","qqqqqqq","zzzzzzzzzz","ggg","zzzzzzz","dddddddddd","jjjjjjj","bbbbb","ttttttt","dddddddd","wwwwwww","vvvvvv","iii","ttttttttt","ggggggg","xx","oooooo","cc","rrrr","qqqq","sssssss","oooo","lllllllll","ii","tttttttttt","uuuuuu","kkkkkkkk","wwwwwwwwww","pppppppppp","uuuuuuuu","yyyyyyy","cccc","ggggg","ddddd","llllllllll","tttt","pppppppp","rrrrrrr","nnnn","x","yyy","iiiiiiiiii","iiiiii","llll","nnnnnnnnnn","aaaaaaaaaa","eeeeeeeeee","m","uuu","rrrrrrrr","h","b","vvvvvvv","ll","vv","mmmmmmm","zzzzz","uu","ccccccc","xxxxxxx","ss","eeeeeeee","llllllll","eeee","y","ppppp","qqqqqq","mmmmmm","gggg","yyyyyyyyy","jjjjjj","rrrrr","a","bbbb","ssssss","sss","ooooo","ffffffffff","kkk","xxxxxxxx","wwwwwwwww","w","iiiiiiii","ffff","dddddd","bbbbbb","uuuuuuuuu","kkkkkkk","gggggggggg","qqqqqqqq","vvvvvvvvv","bbbbbbbbbb","nnnnn","tt","wwww","iiiii","hhhhhhh","zzzzzzzz","ssssssssss","j","fff","bbbbbbb","aaaa","mmmmmmmmmm","jjjjjjjjjj","sssss","yyyyyyyy","hh","q","rrrrrrrrr","mmmmmmmm","wwwww","www","rrr","lllll","uuuuuuuuuu","oo","jjjjjjjjj","dddd","pppp","hhhhhhhhh","kk","gggggggg","xxxxx","vvvv","d","qqqqqqqqq","dd","ggggggggg","t","yyyy","bbb","yyyyyyyyyy","tttttt","ccccc","aa","eeeeee","llllll","kkkkkkkkkk","sssssssss","i","hhhhhh","oooooooooo","wwwwww","ooooooooo","zzzz","k","hhhhhhhh","aaaaa","mmmmm"]
        o = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        self.assertEqual(s.findWords(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)