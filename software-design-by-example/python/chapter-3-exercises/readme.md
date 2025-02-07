What topics were discussed in this chapter?
- Hashing files
    - Hashing files efficiently
    - Relating this efficiency to time complexity, specifically Big-Oh notation
- How to improve the original hashing method provided in the chapter

Exercise 1 (located in chap3.md):

What did I learn from this exercise?
- Aside from simple statistic probability, I feel that my answer to this question can be applied to other problems related to systems and algorithmic design. The odds of collision depend on each other and how many files we are comparing. In a real world scenario, most programs contain many of dependencies. It's always wise to consider all of the dependencies before trying to solve a problem. Otherwise, you may encounter an error that isn't immediately apparent.

Exercise 2 (located in chap3.py):

What did I learn from this exercise?
- To my understanding, when using the hashing module, we can return a byte-like object by calling hashlib.sha256(data).hexdigest on any piece of data.
However, the update() function can be called on a peice of data to update the hash object with a byte-like object. This is useful because it allows you to hash data in chunks, and continuously add those chunks to the hash object. The use case for this would be if the data was being received in the form of streaming data (like our example) or as large files. It would allow you to hash the file piece by piece, rather than loading it all into memory at the beginning of your program.

Exercise 3 (located in chap3.md):

What did I learn from this exercise?
- While I have worked with Big-Oh notation before in previous classes (Data Structures and Algorithms), I have never had to sit down and really consider what is considered "rapid" growth. Doing so allowed me to truly reflect on what I've learned about growth rates and time complexity. I've learned that the most accurate way to compare growth rates for algorithms is by comparing how they grow when the input size is increased. So, that's what I did. I doubled the input size for each type of algorithmic growth rate (constant time, logarithmic, linear, quadratic, cubic, exponential, factorial). The jump from cubic to exponential is what I considered to be most significant when evaluating "rapid growth".

Exercise 4 (located in chap3.md):

What did I learn from this exercise?
- Something that I learned while exploring Python's built in hash function is that the built in function generally has better performance than the functions from the hashlib import. So, with some pieces of data I would use the built in function, while the others would require me to use the hashlib import. This is an idea that I can apply to other imports as well. Then, I can find the most effective way to utilize imported functions, along with built in functions.

Exercise 5 (located in chap3.py):

What did I learn from this exercise?
- To answer the question asked by the book (How evenly deistributed are the hash codes?), I would say that the hash codes are very evenly distributed. From what I can observe, the hash values seem to get more evenly distributed, as the size of my input file grows. After seeing this, I did some searching about why this is case. I found that SHA-256 is designed to produce uniform distributions, so as more unique hash values are introduced, the distribution of these will become more uniform.