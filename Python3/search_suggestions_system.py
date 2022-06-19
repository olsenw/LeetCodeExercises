# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of strings products and a string searchWord.

    Design a system that suggests at most three product names from
    products after each character of searchWord is typed. Suggested
    products should have a common prefix with searchWord. If there are
    more than three products with a common prefix return the tree
    lexicographically minimum products.

    Return a list of lists of the suggested products after each
    character of searchWord is typed.
    '''
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        suggestions = []
        products.sort()
        for i, j in enumerate(searchWord):
            products = [w for w in products if i < len(w) and w[i] == j]
            suggestions.append(products[:3])
        return suggestions

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["mobile","mouse","moneypot","monitor","mousepad"]
        j = "mouse"
        o = [
                ["mobile","moneypot","monitor"],
                ["mobile","moneypot","monitor"],
                ["mouse","mousepad"],
                ["mouse","mousepad"],
                ["mouse","mousepad"]
            ]
        self.assertEqual(s.suggestedProducts(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["havana"]
        j = "havana"
        o = [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
        self.assertEqual(s.suggestedProducts(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["bags","baggage","banner","box","cloths"]
        j = "bags"
        o = [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
        self.assertEqual(s.suggestedProducts(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)