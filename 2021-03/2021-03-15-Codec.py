"""
LeetCode Challenge: Encode and Decode TinyURL (2021-03-15)

TinyURL is a URL shortening service where you enter a URL 
such as https://leetcode.com/problems/design-tinyurl and it 
returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. 
There is no restriction on how your encode/decode algorithm 
should work. You just need to ensure that a URL can be encoded 
to a tiny URL and the tiny URL can be decoded to the original 
URL.
"""

# Runtime: 36 ms (faster than 52.10%); Memory Usage: 14.6 MB
import random
class Codec:
    db = dict()
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        lengthOfString = 4
        shortUrl = f"https://short_url/{''.join(random.choice(string.ascii_letters) for i in range(lengthOfString))}"
        
        # make sure short_url is a unique value
        while shortUrl in self.db: 
            shortUrl = f"https://short_url/{''.join(random.choice(string.ascii_letters) for i in range(lengthOfString))}"
        
        self.db[shortUrl] = longUrl
        return shortUrl
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.db[shortUrl]