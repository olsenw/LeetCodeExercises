# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List
from xml import dom

class Solution:
    '''
    There are n dominoes in a line, and each domino is placed vertically
    upright. In the beginning, some dominoes are simultaneously pushed either to
    the left or the right.

    After each second, each domino that is falling to the left pushes the
    adjacent domino on the left. Similarly, the dominoes falling to the right
    push their adjacent dominoes standing on the right.

    When a vertical domino has dominoes falling on it from both sides, it stays
    still due to the balance of the forces.

    For the purposes of this question, assume that the falling domino expends no
    additional force to a falling or already fallen domino.

    Given a string dominoes representing the initial state where:
    * dominoes[i] = 'L' if the ith domino has been pushed to the left.
    * dominoes[i] = 'R' if the ith domino has been pushed to the right.
    * dominoes[i] = '.' if the ith domino has not been pushed.

    Return a string representing the final state.
    '''
    # idea feels right, but code does not work
    def pushDominoes_fails(self, dominoes: str) -> str:
        dominoes = [c for c in dominoes]
        i = 0
        while i < len(dominoes):
            # if it is already decided skip and move on
            if dominoes[i] != '.':
                i += 1
                continue
            # found a right falling domino left of position i
            r = False
            j = max(i-1,0)
            while j > 0:
                if dominoes[j] != '.':
                    r = dominoes[j] == 'R'
                    j += 1
                    break
                j -= 1
            # found a left falling domino right of position i
            l = False
            k = i+1
            while k < len(dominoes):
                if dominoes[k] != '.':
                    l = dominoes[k] == 'L'
                    k -= 1
                    break
                k += 1
            # both a left and right domino has been found (find midpoint)
            if l and r:
                m = j + (k - j) // 2
                for a in range(j,m):
                    dominoes[a] = 'R'
                for b in range(m+1,k+1):
                    dominoes[b] = 'L'
            # only a left falling domino has been found
            elif l:
                for a in range(j,k+1):
                    dominoes[a] = 'L'
            # only a right falling domino has been found
            elif r:
                for b in range(j,k+1):
                    dominoes[b] = 'R'
            # nothing falls over (motion canceled out)
            else:
                pass
            # advance position to unconsidered position
            i = k + 1
        return ''.join(dominoes)

    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        r = [0] * n
        for i in range(1,n):
            if dominoes[i] == '.' and (dominoes[i-1] == 'R' or r[i-1]):
                r[i] = r[i-1] + 1
        l = [0] * n
        for i in range(n-2,-1,-1):
            if dominoes[i] == '.' and (dominoes[i+1] == 'L' or l[i+1]):
                l[i] = l[i+1] + 1
        a = ''
        for k,(i,j) in enumerate(zip(r,l)):
            if dominoes[k] != '.':
                a += dominoes[k]
            elif i and j:
                if i == j:
                    a += '.'
                elif i < j:
                    a += 'R'
                else:
                    a += 'L'
            elif i:
                a += 'R'
            elif j:
                a += 'L'
            else:
                a += '.'
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "RR.L"
        o = "RR.L"
        self.assertEqual(s.pushDominoes(i), o)

    def test_two(self):
        s = Solution()
        #    01234567890123
        i = ".L.R...LR..L.."
        # r  00001230012000
        # l  10003210021000
        o = "LL.RR.LLRRLL.."
        self.assertEqual(s.pushDominoes(i), o)

    def test_three(self):
        s = Solution()
        i = ".R"
        o = ".R"
        self.assertEqual(s.pushDominoes(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)