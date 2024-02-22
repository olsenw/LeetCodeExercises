# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string sentence that consist of words separated by spaces. Each word
    consists of lowercase and uppercase letters only.

    Convert the sentence to "Goat Latin" using the following rules:
    * If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to
      the end of the word.
    * If a word begins with a consonant (ie, not a vowel), remove the first
      letter and append it to the end, then add "ma".
    * Add one letter 'a' to the end of each word per its word index in the
      sentence, starting with 1.
    
    Return the final sentence representing the conversion from sentence to Goat
    Latin.
    '''
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        for i in range(len(sentence)):
            if sentence[i][0] not in "aeiouAEIOU":
                sentence[i] = sentence[i][1:] + sentence[i][:1]
            sentence[i] += "ma"
            sentence[i] += "a" * (i + 1)
        return ' '.join(sentence)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "I speak Goat Latin"
        o = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
        self.assertEqual(s.toGoatLatin(i), o)

    def test_two(self):
        s = Solution()
        i = "The quick brown fox jumped over the lazy dog"
        o = "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
        self.assertEqual(s.toGoatLatin(i), o)

    def test_three(self):
        s = Solution()
        i = "Each word consists of lowercase and uppercase letters only"
        o = "Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa"
        self.assertEqual(s.toGoatLatin(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)