# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
There is a browser of one tab which starts on a homepage. It is possible to
visit another url. It is also possible to go forward and back n steps in the
history.
'''
class BrowserHistory:
    '''
    Initializes the object with the homepage of the browser.
    '''
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.future = []

    '''
    Visits url from the current page. Also clears the forward history.
    '''
    def visit(self, url: str) -> None:
        self.history.append(url)
        self.future.clear()

    '''
    Move steps back in history. If there are fewer urls in the history than
    steps, go back only the possible urls. Return the url after moving back in
    history at most steps.
    '''
    def back(self, steps: int) -> str:
        while len(self.history) > 1 and steps:
            self.future.append(self.history.pop())
            steps -= 1
        return self.history[-1]

    '''
    Move steps forward in history. If there are more steps forward than history
    go forward only the possible urls. Return the current url after forwarding
    in history at most steps.
    '''
    def forward(self, steps: int) -> str:
        while len(self.future) and steps:
            self.history.append(self.future.pop())
            steps -= 1
        return self.history[-1]

'''
Smarter way would be to have a single list that is truncated on a visit and uses
an index to keep track of forward/backward in time.

Kind of like the two stack solution though... but it is not as good.
'''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        b = BrowserHistory("leetcode.com")
        b.visit("google.com")
        b.visit("facebook.com")
        b.visit("youtube.com")
        self.assertEqual(b.back(1), "facebook.com")
        self.assertEqual(b.back(1), "google.com")
        self.assertEqual(b.forward(1), "facebook.com")
        b.visit("linkedin.com")
        self.assertEqual(b.forward(2), "linkedin.com")
        self.assertEqual(b.back(2), "google.com")
        self.assertEqual(b.back(7), "leetcode.com")

if __name__ == '__main__':
    unittest.main(verbosity=2)