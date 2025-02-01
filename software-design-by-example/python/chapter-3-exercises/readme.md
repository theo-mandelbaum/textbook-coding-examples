Exercise 1 (located in chap3.md):



Exercise 2 (located in chap3.py):

What did I learn from this exercise?
- To my understanding, when using the hashing module, we can return a byte-like object by calling hashlib.sha256(data).hexdigest on any piece of data.
However, the update() function can be called on a peice of data to update the hash object with a byte-like object. This is useful because it allows you to hash data in chunks, and continuously add those chunks to the hash object. The use case for this would be if the data was being received in the form of streaming data (like our example) or as large files. It would allow you to hash the file piece by piece, rather than loading it all into memory at the beginning of your program.

Exercise 3 (located in chap3.md):

What did I learn from this exercise?
- While I have worked with Big-Oh notation before in previous classes (Data Structures and Algorithms), I have never had to sit down and really consider what is considered "rapid" growth. Doing so allowed me to truly reflect on what I've learned about growth rates and time complexity. I've learned that the most accurate way to compare growth rates for algorithms is by comparing how they grow when the input size is increased. So, that's what I did. I doubled the input size for each type of algorithmic growth rate (constant time, logarithmic, linear, quadratic, cubic, exponential, factorial). The jump from cubic to exponential is what I considered to be most significant when evaluating "rapid growth".

Exercise 4 ()