# -*- coding: utf-8 -*-
"""Chapter_04.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/nceder/qpb4e/blob/main/code/Chapter%2004/Chapter_04.ipynb

# 4 The absolute basics

# 4.3 Variables and assignments
"""

a = [1, 2, 3]
b = a
c = b
b[1] = 5
print(a, b, c)

a = 1
b = a
c = b
b = 5
print(a, b, c)

x = "Hello"
print(x)

x = 5
print(x)

del x
print(x)

"""# 4.4 Optional type hints in Python"""

def add_ints(x: int, y: int) -> int:      #A
     return x + y

p: int = 2.3                               #B
z = add_ints(1, 2)
w = add_ints(1.5, 2.5)                     #C

"""# 4.5 Expressions"""

x = 3
y = 5
z = (x + y) / 2

"""### Try This: variables and expressions
In the cell below, create some variables. What happens when you try to put spaces, dashes, or other nonalphanumeric characters in the variable name? Play around with a few complex expressions, such as x = 2 + 4 * 5 - 6 / 3. Use parentheses to group the numbers in different ways, and see how that changes the result compared with the original ungrouped expression.
"""

# enter you experiments in this cell

"""# 4.6 Strings"""

x = "\tThis string starts with a \"tab\"."
x = "This string contains a single backslash(\\)."

x = "Hello, World"
x = 'Hello, World'

x = "Don't need a backslash"
x = 'Can\'t get by without a backslash'
x = "Backslash your \" character!"
x = 'You can leave the " alone'

# This Python code will cause an ERROR -- you can't
# split the string across two lines.
x = "This is a misguided attempt to
put a newline into a string without using backslash-n"

x = """Starting and ending a string with triple " or ' characters
permits embedded newlines, and the use of " and ' without
backslashes"""

"""# 4.7 Numbers"""

5 + 2 - 3 * 2

5 / 2          # floating-point result with normal division

5 / 2.0        # also a floating-point result

5 // 2         # integer result with truncation when divided using '//'

30000000000    # This would be too large to be an int in many languages

30000000000 * 3

30000000000 * 3.0

2.0e-8         # Scientific notation gives back a float

3000000 * 3000000

int(200.2)

int(2e2)

float(200)

"""## 4.7.4 Complex numbers"""

(3+2j)

3 + 2j - (4+4j)

(1+2j) * (3+4j)

1j * 1j

z = (3+5j)
z.real

z.imag

"""## 4.7.5 Advanced complex-number functions"""

import cmath
cmath.sqrt(-1)

"""### Try This: Manipulating strings and numbers
In the cell below, create some string and number variables (integers, floats, and complex numbers). Experiment a bit with what happens when you do operations with them, including across types. Can you multiply a string by an integer, for example, or by a float or complex number? Also, load the math module and try out a few of the functions; then load the cmath module and do the same. What happens if you try to use one of those functions on an integer or float after loading the cmath module? How might you get the math module functions back?
"""

# enter you experiments in this cell

"""# 4.9 Getting input from the user"""

name = input("Name? ")

print(name)

age = int(input("Age? "))

print(age)

"""### Try this: Getting input
Experiment with the input() function to get string and integer input. Using code similar to the previous code, what is the effect of not using int() around the call to input()for integer input? Can you modify that code to accept a float—say, 28.5? What happens if you deliberately enter the wrong type of value? Examples include a float in which an integer is expected and a string in which a number is expected—and vice versa.

"""

# enter you experiments in this cell

"""###Quick Check: Pythonic style
Which of the following variable and function names do you think are not good Pythonic style? Why?

`bar(), varName, VERYLONGVARNAME, foobar, longvarname, foo_bar(), really_very_long_var_name`

* `bar(`: Not good, not legal, includes symbol
* `varName`: Not good, mixed case
* `VERYLONGVARNAME`: Not good, long, all caps, hard to read
* `foobar`: Good
* `longvarname`: Good, although underscores to separate words would be better
* `foo_bar()`: Good
* `really_very_long_var_name`: Long, but good if all of the words are needed, perhaps to distinguish among similar variables


"""

