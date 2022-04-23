# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

'''
TinyURL is a URL shortening service where a URL such as 
https://leetcode.com/problems/design-tinyurl and it returns a short URL
such as http://tinyurl.com/4e9iAk . Design a class to encode a URL and
decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work.
Just need to ensure that a URL can be encoded to a tiny URL and the tiny
URL can be decoded to the original URL.
'''
# does no encoding/decoding but passes the tests
class Codec_Simple:

    '''
    Returns a tiny URL for the given longUrl
    '''
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        return longUrl

    '''
    Returns the original long URL for the given shortUrl. It is
    guaranteed that the given shortUrl was encoded by the same object.
    '''
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl

# based on discusion post that is a companion to this problem
# https://leetcode.com/discuss/interview-question/124658/Design-a-URL-Shortener-(-TinyURL-)-System/
# keeps track to all longUrls that have been encoded in a list and keeps
# mapping from longUrl to index in list.
class Codec:

    def __init__(self):
        # list of all long urls
        self.l = []
        # mapping of long urls to there index in list
        self.m = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.m:
            return self.m[longUrl]
        i = str(len(self.l))
        self.l.append(longUrl)
        self.m[longUrl] = i
        return i

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.l[int(shortUrl)]

class UnitTesting(unittest.TestCase):

    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.decode(codec.encode(url))

    def test_one(self):
        s = Codec()
        url = "https://leetcode.com/problems/design-tinyurl"
        self.assertEqual(s.decode(s.encode(url)), url)

if __name__ == '__main__':
    unittest.main(verbosity=2)