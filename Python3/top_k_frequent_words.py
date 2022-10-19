# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List
import heapq

class Solution:
    # note Counter.most_common sorts on first occurrence not lowest alphabetical
    # O(n log n) n to create counter and n log n to sort
    def topKFrequent_Counter(self, words: List[str], k: int) -> List[str]:
        return [a for a,_ in sorted(Counter(words).items(), key=lambda x: (-x[1], x[0]))[:k]]

    # O(n log k) n to create counter and n log k for min heap size k
    # O(n + k) because k <= n, O(n + k) => O(2n) => O(n)
    def topKFrequent_min_heap(self, words: List[str], k: int) -> List[str]:
        # needed to define custom comparator for tuples in heap
        class record:
            def __init__(self, s, n) -> None:
                self.s, self.n = s, n
            def __lt__(self, other):
                if self.n <= other.n:
                    return self.s > other.s if self.n == other.n else True
                return False
        h = []
        for i,j in Counter(words).items():
            if len(h) < k:
                # need to change how string compared (inverse)
                heapq.heappush(h, record(i,j))
            else:
                # need to change how string compared (inverse)
                heapq.heappushpop(h, record(i,j))
        return [heapq.heappop(h).s for _ in range(len(h))][::-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["i","love","leetcode","i","love","coding"]
        j = 2
        o = ["i","love"]
        self.assertEqual(s.topKFrequent(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["the","day","is","sunny","the","the","the","sunny","is","is"]
        j = 4
        o = ["the","is","sunny","day"]
        self.assertEqual(s.topKFrequent(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["i","love","leetcode","i","love","coding"]
        j = 3
        o = ["i","love","coding"]
        self.assertEqual(s.topKFrequent(i,j), o)

    def test_four(self):
        s = Solution()
        i = ["aaa", "aa", "a"]
        j = 1
        o = ["a"]
        self.assertEqual(s.topKFrequent(i,j), o)

    def test_five(self):
        s = Solution()
        i = ["a", "aa", "aaa"]
        j = 1
        o = ["a"]
        self.assertEqual(s.topKFrequent(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)