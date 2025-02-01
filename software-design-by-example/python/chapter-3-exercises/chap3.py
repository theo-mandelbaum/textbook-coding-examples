# Exercise 2: Streaming I/O
# Question:
# A streaming API delivers data one piece at a time rather than all at once.
# Read the documentation for the update method of hashing objects in Python’s hashing module
# and rewrite the duplicate finder from this chapter to use it.

import sys
from hashlib import sha256

def same_bytes(left_name, right_name):
    left_bytes = open(left_name, "rb").read()
    right_bytes = open(right_name, "rb").read()
    return left_bytes == right_bytes

def find_groups(filenames):
    groups = {}
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = sha256().update(data)
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)
    return groups

def find_duplicates(filenames):
    matches = []
    for left in filenames:
        for right in filenames:
            if left != right and same_bytes(left, right):
                matches.append((left, right))
    return matches

if __name__ == "__main__":
    groups = find_groups(sys.argv[1:])
    for group in groups.values():
        duplicates = find_duplicates(list(group))
        for left, right in duplicates:
            print(left, right)