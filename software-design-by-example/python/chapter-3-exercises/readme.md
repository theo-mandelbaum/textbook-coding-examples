Exercise 1 (located in chap3.md):



Exercise 2( located in chap3.py):

What did I learn from this exercise?
- To my understanding, when using the hashing module, we can return a byte-like object by calling hashlib.sha256(data).hexdigest on any piece of data.
However, the update() function can be called on a peice of data to update the hash object with a byte-like object. This is useful because it allows you to hash data in chunks, and continuously add those chunks to the hash object. The use case for this would be if the data was being received in the form of streaming data (like our example) or as large files. It would allow you to hash the file piece by piece, rather than loading it all into memory at the beginning of your program.

