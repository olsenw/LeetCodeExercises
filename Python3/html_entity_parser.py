# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    HTML entity parser is the parser that takes HTML code as input and replace
    all the entities of the special character by the characters itself.

    The special characters and their entities for HTML are:
    * Quotation Mark: the entity is &quot; and symbol character is ".
    * Single Quote Mark: the entity is &apos; and symbol character is '.
    * Ampersand: the entity is &amp; and symbol character is &.
    * Greater Than Sign: the entity is &gt; and symbol character is >.
    * Less Than Sign: the entity is &lt; and symbol character is <.
    * Slash: the entity is &frasl; and symbol character is /.

    Given the input text string to the HTML parser, implement the entity parser.

    Return the text after replacing the entities by the special characters.
    '''
    # works but slower
    def entityParser_passes(self, text: str) -> str:
        answer = ""
        token = ""
        for c in text:
            if c == '&':
                answer += token
                token = c
            elif len(token) > 0 and c == ';':
                token += c
                if token == "&quot;":
                    answer += "\""
                elif token == "&apos;":
                    answer += "'"
                elif token == "&amp;":
                    answer += "&"
                elif token == "&gt;":
                    answer += ">"
                elif token == "&lt;":
                    answer += "<"
                elif token == "&frasl;":
                    answer += "/"
                else:
                    answer += token
                token = ""
            elif len(token) > 0:
                token += c
            else:
                answer += c
        return answer + token

    def entityParser(self, text: str) -> str:
        return text.replace("&quot;","\"").replace("&apos;","'").replace("&gt;",">").replace("&lt;","<").replace("&frasl;","/").replace("&amp;","&")

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "&amp; is an HTML entity but &ambassador; is not."
        o = "& is an HTML entity but &ambassador; is not."
        self.assertEqual(s.entityParser(i), o)

    def test_two(self):
        s = Solution()
        i = "and I quote: &quot;...&quot;"
        o = "and I quote: \"...\""
        self.assertEqual(s.entityParser(i), o)

    def test_three(self):
        s = Solution()
        i = "leetcode.com&frasl;problemset&frasl;all"
        o = "leetcode.com/problemset/all"
        self.assertEqual(s.entityParser(i), o)

    def test_four(self):
        s = Solution()
        i = "&&gt;"
        o = "&>"
        self.assertEqual(s.entityParser(i), o)

    def test_five(self):
        s = Solution()
        i = "&&&"
        o = "&&&"
        self.assertEqual(s.entityParser(i), o)

    def test_six(self):
        s = Solution()
        i = "&amp;quot;&amp;apos;&amp;amp;&amp;gt;&amp;lt;&amp;frasl;"
        o = "&quot;&apos;&amp;&gt;&lt;&frasl;"
        self.assertEqual(s.entityParser(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)