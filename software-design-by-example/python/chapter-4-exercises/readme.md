Exercise 1 (located in coding_exercises/looping.py): Looping
Rewrite the matchers so that a top-level object manages a list of matchers, none of which know about any of the others. Is this design simpler or more complicated than the Chain of Responsibility design?

Conclusion:
- The design of having one top-level object that manages a list of matchers is simpler than the Chain of Responsibility design. This is because the top-level class handles the sequence of matchers by iterating over a list, centralizing the control of the matchers. The matchers do not need to be aware of the sequence. The matchers also do not need to know how to interact withe each other.


Exercise 2: Length Plus One
Why does the upper bound of the loop in the final version of Any run to len(text) + 1?

Conclusion:
- The loop in Any runs to length plus one because we need to be able to match the substring of an empty string at the end of a the text. Runnning to len(text) + 1 allows us to check the position beyond the last character in our text, checking for a empty string at the end.


Exercise 3 (located in coding_exercises/looping.py): Find One or More
Extend the regular expression matcher to support +, meaning “match one or more characters”.


Exercise 4 (located in coding_exercises/sets.py): Match Sets of Characters
1. Add a new matching class that matches any character from a set, so that Charset('aeiou') matches any lower-case vowel.

2. Create a matcher that matches a range of characters. For example, Range("a", "z") matches any single lower-case Latin alphabetic character. (This is just a convenience matcher: ranges can always be spelled out in full.)

3. Write some tests for your matchers.

Conclusion | What did I learn?:
- At first I thought that I would have to loop through and recursively call _match, the same way that Dr. Wilson did in glob_null. After writing my code, I realized that the 'in' operation in python involves a loop or some kind of similar iteration method. So, I am actually am looping. This, along with recent coursework in Applied Algorithms has allowed me to think about what is really happening in my helper functions and how that relates to the algorithms that I use.