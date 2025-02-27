# Exercise 1: Looping

"""Rewrite the matchers so that a top-level object manages a list of matchers, 
none of which know about any of the others. 
Is this design simpler or more complicated than the Chain of Responsibility design?"""

class TopMatcher:
    def __init__(self):
        self.matchers = []
    
    def add_matcher(self, matcher):
        self.matchers.append(matcher)

    def matcher(self, text):
        start = 0
        for matcher in self.matchers:
            start = matcher._match(text, start)
            if start is None:
                return False
            return start == len(text)


# [null]
class Null:
    def _match(self, text, start):
        return start
# [/null]

# [any]
class Any:
    def _match(self, text, start):
        for i in range(start, len(text) + 1):
            if i == len(text):
                return i
        return None
# [/any]

# [either]
class Either:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def _match(self, text, start):
        for pat in [self.left, self.right]:
            end = pat._match(text, start)
            if end is not None:
                return end
        return None
# [/either]

# [lit]
class Lit:
    def __init__(self, chars):
        self.chars = chars

    def _match(self, text, start):
        end = start + len(self.chars)
        if text[start:end] != self.chars:
            return None
        return end
# [/lit]
