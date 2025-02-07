# Exercise 5: How Good is SHA-256?

# Question:

# 1. Write a function that calculates the SHA-256 hash code of each unique line of a text file.
# 2. Convert the hex digests of those hash codes to integers.
# 3. Plot a histogram of those integer values with 20 bins.
# 4. How evenly distributed are the hash codes? How does the distribution change as you process larger files

# This code can be run on on command line using "python3 exercise5.py testing_files/histogram_file.txt", while in the "chapter-3-exercises" directory

import sys
from hashlib import sha256
import matplotlib.pyplot as plt

def sha256_histogram(filename):
    values_to_plot = set()
    with open(filename, 'r') as file:
        for line in file:
            hash_object = sha256()
            hash_object.update(line.strip().encode())
            hex_digest_int = int(hash_object.hexdigest(), 16)
            normalized_val = hex_digest_int % 10**10 # Normalize the value so that it is not too large for plt.hist()
            values_to_plot.add(normalized_val)
    
    plt.hist(list(values_to_plot), bins=20)
    plt.xlabel('Hash Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of SHA-256 Hash Values')
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python exercise5.py <filename>")
    else:
        sha256_histogram(sys.argv[1])