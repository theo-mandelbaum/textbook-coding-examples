import math

# The final version of call declares a parameter called *args to capture all the positional arguments of the method being called and then spreads them in the actual call
# Modify it to capture and spread named arguments as well.

def call(thing, method_name, *args, **kwargs):
    method = find(thing["_class"], method_name)
    return method(thing, *args, **kwargs)

# A recursive function is one that calls itself, either directly or indirectly
# Modify the find function that finds a method to call so that it uses recursion instead of a loop. Which version is easier to understand? Which version is more efficient?

def find(cls, method_name):
    if cls is None:
        raise NotImplementedError("method_name")
    if method_name in cls:
        return cls[method_name]
    return find(cls["_parent"], method_name)

# Python type method reports the most specific type of an object, while isinstance determines whether an object inherits from a type either directly or indirectly
# Add your own versions of both to dictionary-based objects and classes.

def type(object):
    return object["_classname"]

def isinstance(object, type):
    object_to_test = object
    while (object["_parent"] != None):
        if (object_to_test["_classname"] == type):
            return True
        object_to_test = object_to_test["_parent"]
    return False

# Implement multiple inheritance using dictionaries
# Does your implementation look methods up in the same order as Python would?

student_year = 3
major = "CS"

def gpa_calculator(thing, total_grade_points, total_credit_hours):
    return total_grade_points / total_credit_hours

def student_new(major, year):
    return {
        "major": major,
        "year": year,
        "_class": Student
    }

Student = {
    "gpa_calculator": gpa_calculator,
    "_classname": "Student",
    "_parent": None,
    "_new": student_new
}

# Explain the differences between class methods and static methods.
'''
While both class methods and static methods are bound to a class and not an object of a class, there are a few differences
The first main difference is that a class method takes "cls" as its first parameter, representing the class itself
The second main difference is that class methods are capable of modifying the class state, while static methods cannot
'''
# Implement both using dictionaries.
'''
The make() function is one of my implementations of class methods. My other implementation is in the find() method on line 13.
Both theo_new() and christian_new() are implmentations of static methods
'''

def make(cls, *args):
    return cls["_new"](*args)

def theo_new(major, year):
    return make(Student, major, year) | {
        "major": major,
        "year": year,
        "_class": Theo
    }

Theo = {
    "year": student_year,
    "major": major,
    "_classname": "Theo",
    "_parent": Student,
    "_new": theo_new
}

def christian_new(major, year):
    return make(Student, major, year) | {
        "major": major,
        "year": year,
        "_class": Christian
    }

Christian = {
    "year": student_year,
    "major": major,
    "_classname": "Christian",
    "_parent": Student,
    "_new": christian_new
}

examples = [make(Theo, "CS", 3), make(Christian, "CS", 2)]
for ex in examples:
    y = ex["year"]
    d = call(ex, "gpa_calculator", 12, 3)
    print(f"{y}: {d:.2f}")