# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two images, img1 and img2, represented as binary, square matrices of
    size n x n. A binary matrix has only 0's and 1's as values.

    An image can be translated by sliding all the 1 bits left, right, up, and/or
    down any number of units. The translated image is then placed on top of the
    other image. the overlap is calculated by counting the number of positions
    that have a 1 in both images.

    Note that a translation does not include any kind of rotation. Any 1 bits
    that are translated outside of the matrix borders are erased.

    Return the largest possible overlap.
    '''
    # brute shifting (failed convolution start)
    # very slow implementation
    # O(n^4) time
    def largestOverlap_tle(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        best = 0
        n = len(img1)
        m = 2 * n + 1
        mat = [[0] * (m) for _ in range(m)]
        for i in range(n):
            for j in range(n):
                mat[i + n - 1][j + n - 1] = img2[i][j]
        for i in range(m):
            for j in range(m):
                count = 0
                for x in range(n):
                    if i + x == m:
                        break
                    for y in range(n):
                        if j + y == m:
                            break
                        if img1[x][y] and mat[i + x][j + y]:
                            count += 1
                best = max(best, count)
        return best

    # smarter way to do the above
    # O(n^4) time
    # O(1) space
    def largestOverlap_shift_leetcode(self, A: List[List[int]], B: List[List[int]]) -> int:
        dim = len(A)

        def shift_and_count(x_shift, y_shift, M, R):
            """ 
                Shift the matrix M in up-left and up-right directions 
                  and count the ones in the overlapping zone.
                M: matrix to be moved
                R: matrix for reference

                moving one matrix up is equivalent to
                moving the other matrix down
            """
            left_shift_count, right_shift_count = 0, 0
            for r_row, m_row in enumerate(range(y_shift, dim)):
                for r_col, m_col in enumerate(range(x_shift, dim)):
                    if M[m_row][m_col] == 1 and M[m_row][m_col] == R[r_row][r_col]:
                        left_shift_count += 1
                    if M[m_row][r_col] == 1 and M[m_row][r_col] == R[r_row][m_col]:
                        right_shift_count += 1

            return max(left_shift_count, right_shift_count)

        max_overlaps = 0
        # move one of the matrice up and left and vice versa.
        # (equivalent to move the other matrix down and right)
        for y_shift in range(0, dim):
            for x_shift in range(0, dim):
                # move the matrix A to the up-right and up-left directions
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, A, B))
                # move the matrix B to the up-right and up-left directions
                #  which is equivalent to moving A to the down-right and down-left directions 
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, B, A))

        return max_overlaps

    # finds all the valid transformations (1 cell in A to B) and trys them
    # O(n^4) time
    # O(n^2) space
    def largestOverlap_linear_algebra_leetcode(self, A: List[List[int]], B: List[List[int]]) -> int:

        dim = len(A)

        def non_zero_cells(M):
            ret = []
            for x in range(dim):
                for y in range(dim):
                    if M[x][y] == 1:
                        ret.append((x, y))
            return ret

        transformation_count = defaultdict(int)
        max_overlaps = 0

        A_ones = non_zero_cells(A)
        B_ones = non_zero_cells(B)

        for (x_a, y_a) in A_ones:
            for (x_b, y_b) in B_ones:
                vec = (x_b - x_a, y_b - y_a)
                transformation_count[vec] += 1
                max_overlaps = max(max_overlaps, transformation_count[vec])

        return max_overlaps

    # convolution with all possible kernels
    # note the use of numpy to perform faster
    # O(n^4) time
    # O(n^2) space
    def largestOverlap_convolution_kernels_leetcode(self, A: List[List[int]], B: List[List[int]]) -> int:

        import numpy as np
        A = np.array(A)
        B = np.array(B)

        dim = len(A)
        # extend the matrix to a wider range for the later kernel extraction.
        B_padded = np.pad(B, dim-1, mode='constant', constant_values=(0, 0))

        max_overlaps = 0
        for x_shift in range(dim*2 - 1):
            for y_shift in range(dim* 2 - 1):
                # extract a kernel from the padded matrix
                kernel = B_padded[x_shift:x_shift+dim, y_shift:y_shift+dim]
                # convolution between A and kernel
                non_zeros = np.sum(A * kernel)
                max_overlaps = max(max_overlaps, non_zeros)

        return max_overlaps

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1,0],[0,1,0],[0,1,0]]
        j = [[0,0,0],[0,1,1],[0,0,1]]
        o = 3
        self.assertEqual(s.largestOverlap(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1]]
        j = [[1]]
        o = 1
        self.assertEqual(s.largestOverlap(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[0]]
        j = [[0]]
        o = 0
        self.assertEqual(s.largestOverlap(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)