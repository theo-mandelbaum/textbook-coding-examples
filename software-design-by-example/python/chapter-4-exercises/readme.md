Exercise 1 (located in looping.py): Looping
Rewrite the matchers so that a top-level object manages a list of matchers, none of which know about any of the others. Is this design simpler or more complicated than the Chain of Responsibility design?

Conclusion:
- The design of having one top-level object that manages a list of matchers is simpler than the Chain of Responsibility design. This is because the top-level class handles the sequence of matchers by iterating over a list, centralizing the control of the matchers. The matchers do not need to be aware of the sequence. The matchers also do not need to know how to interact withe each other.


Exercise 2: Length Plus One
Why does the upper bound of the loop in the final version of Any run to len(text) + 1?

Conclusion:
- The loop in Any runs to length plus one because we need to be able to match the substring of an empty string at the end of a the text. Runnning to len(text) + 1 allows us to check the position beyond the last character in our text, checking for a empty string at the end.
