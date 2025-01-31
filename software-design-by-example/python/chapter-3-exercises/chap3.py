# Exercise 2: Streaming I/O
# Question:
# A streaming API delivers data one piece at a time rather than all at once.
# Read the documentation for the update method of hashing objects in Python’s hashing module
# and rewrite the duplicate finder from this chapter to use it.

import sys
import hashlib

def same_bytes(left_name, right_name):
    left_bytes = open(left_name, "rb").read()
    right_bytes = open(right_name, "rb").read()
    return left_bytes == right_bytes

def find_duplicates(filenames):
    matches = []
    for left in filenames:
        for right in filenames:
            if same_bytes(left, right):
                matches.append((left, right))
    return matches

if __name__ == "__main__":
    duplicates = find_duplicates(sys.argv[1:])
    for (left, right) in duplicates:
        print(left, right)