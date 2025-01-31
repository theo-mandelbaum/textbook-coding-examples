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

