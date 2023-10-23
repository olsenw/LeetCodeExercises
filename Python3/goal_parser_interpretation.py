# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a goal parser that can interpret a string command. The command
    consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal
    Parser will interpret "G" as the string "G", "()" as the string "o", and
    "(al)" as the string "al". The interpreted stings are then concatenated in
    the original order.

    Given the string command, return the Goal Parser's interpretation of
    command.
    '''
    def interpret(self, command: str) -> str:
        answer = ""
        index = 0
        while index < len(command):
            if command[index] == "G":
                answer += "G"
            else:
                if command[index + 1] == ")":
                    answer += "o"
                    index += 1
                else:
                    answer += "al"
                    index += 3
            index += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "G()(al)"
        o = "Goal"
        self.assertEqual(s.interpret(i), o)

    def test_two(self):
        s = Solution()
        i = "G()()()()(al)"
        o = "Gooooal"
        self.assertEqual(s.interpret(i), o)

    def test_three(self):
        s = Solution()
        i = "(al)G(al)()()G"
        o = "alGalooG"
        self.assertEqual(s.interpret(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)