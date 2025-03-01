"""
1. Add a new matching class that matches any character from a set, so that Charset('aeiou') matches any lower-case vowel.

2. Create a matcher that matches a range of characters. For example, Range("a", "z") matches any single lower-case Latin alphabetic character. (This is just a convenience matcher: ranges can always be spelled out in full.)

3. Write some tests for your matchers.
"""

# Matching class that matches any character from a set
class Charset:
    def __init__(self, set):
        self.set = set

    def _match(self, char):
        if char in self.set:
            return char
        return None


# Matcher that matches a range of characters
# Note: the 'ord' function in python returns the Unicode (integer representation) point for a char.
class Range:
    def __init__(self, start, end):
        self.range = range(ord(start), ord(end)+1)
    
    def _match(self, char):
        if ord(char) in self.range:
            return char
        return None



# [tests]
def test_charset_match():
    # /g/ matches Charset('asdghyry')
    assert Charset('asdghyry')._match("g")

def test_charset_no_match():
    # /g/ doesn't match Charset('asdhyry')
    assert not Charset('asdhyry')._match("g")

# [tests]
def test_range_match():
    # /g/ matches Range("a", "y")
    assert Range("a", "y")._match("g")

def test_range_no_match():
    # /g/ doesn't match Range("a", "d")
    assert not Range("a", "d")._match("g")

if __name__ == "__main__":
    test_charset_match()
    test_charset_no_match()
    test_range_match()
    test_range_no_match()
    print("All tests passed!")