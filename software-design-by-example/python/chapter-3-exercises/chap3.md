### This chapter is based on the file comparison algorithms in brute_force_1.py and dup.py
### Read the readme for more information on the provided files

# Exercise 1: Odds of Collision

## Question: 

If hashes were only 2 bits long, then the chances of collision with each successive file assuming no previous collision are:

| Number of Files | Odds of Collision |
|-----------------|-------------------|
| 1	              | 0%                |
| 2	              | 25%               |
| 3	              | 50%               |
| 4	              | 75%               |
| 5	              | 100%              |

A colleague of yours says this means that if we hash four files, there’s only a 75% chance of any collision occurring. What are the actual odds?

## My Calculation:

So, we are comparing four files, all 2 bits long. We know the chances of collision increase by 25% for each file that is compared, creating the chart that we have above.

We know that our colleague's interpretation is wrong because the odd's of collision depend on each other and how many files there are.
Since it is dependent, we cannot just take the fourth percentage (75%). We must take into account that files 2-4 all have a chance of collision

The way to calculate this is finding the odds of no collision and then subtracting that number from 1.

Based on our odds of collision being .25, .50, and .75, we can say that, inversely, our odds of no collision are .75, .50, and .25.

So to find our odds of collision, when hashing four files, we will do the following calculation:

Odds of collision: 1 - (.75 x .50 x .25) = 1 - .09375 = 0.90625

# Exercise 2 can be found in chap3.py


# Exercise 3: Big Oh

## Question:

Chapter 1 said that as the number of components in a system grows, the complexity of the system increases rapidly. How fast is “rapidly” in big-oh terms?

## My Conclusion:

After revisiting Big-Oh time complexity through my current coursework and the readings in this book, I have concluded that rapidly in big-oh terms includes both exponential and factorial growth rates. The largest difference in growth appears in those two (exponential and factorial) time complexities. While O(n^3) does grow faster than O(n), the difference between two polynomial terms is not as large as the difference between a polynomial term and an exponential term.

For example, say the input size of an algorithm increased by a factor of two. To find the increase in runnning time, we would solve for the output of the following equation:

f(2n) / f(n)

# Let's use f(n) = n^3:

f(2n) = (2n)^3 = 8n^3
f(n) = n^3

So, f(2n) / f(n) = 8n^3 / n^3,
Which allows us to cancel out the n^3 in the numerator and denominator,
resulting in f(2n) / f(n) = 8

This means that the running time of n^3 increases by 8, as the input size of the algorithm increase by a factor of 2

# Now, let's use f(n) = 2^n

f(2n) = 2^(2n) = (2^n) * (2^n)
f(n) = 2^n

So, f(2n) / f(n) = (2^n) * (2^n) / 2^n
Here we can cancel out a 2^n in the numerator and get rid of the 2^n in the denominator,
which results in f(2n) / f(n) = 2^n

This means that the running time of 2^n increases by 2^n, as the input size of the algorithm increase by a factor of 2

## Final statment

As you can see, the difference between n^3 and 2^n is huge, even when the input size is only increasing by a factor of 2. So, I would consider any term 2^n and larger to be a "rapid" growth rate.
