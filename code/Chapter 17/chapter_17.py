# -*- coding: utf-8 -*-
"""Chapter_17.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/nceder/qpb4e/blob/main/code/Chapter%2017/Chapter_17.ipynb

# 17 Data types as objects

# 17.1 Types are objects, too
"""

type(5)

type(['hello', 'goodbye'])

type_result = type(5)
type(type_result)

"""# 17.2 Using types"""

type("Hello") == type("Goodbye")

type("Hello") == type(5)

"""# 17.3 Types and user-defined classes"""

class A:
    pass

class B(A):
    pass

b = B()
type(b)

b.__class__

b_class = b.__class__
b_class == B

b_class.__name__

b_class.__bases__

class C:
    pass

class D:
    pass

class E(D):
    pass

x = 12
c = C()
d = D()
e = E()
isinstance(x, E)

isinstance(c, E)             #A

isinstance(e, E)

isinstance(e, D)             #B

isinstance(d, E)                #C

y = 12
isinstance(y, type(5))             #D

issubclass(C, D)

issubclass(E, D)

issubclass(D, D)           #E

issubclass(e.__class__, D)

"""### Quick Check: Types
Suppose that you want to make sure that object `x` is a `list` before you try appending to it. What code would you use? What would be the difference between using `type()` and `isinstance()`? Would this be the look before you leap (LBYL) or easier to ask forgiveness than permission (EAFP) of programming? What other options might you have besides checking the type explicitly?

#### Solution
```python
x = []
if isinstance(x, list):
    print("is list")
    ```
Using type would get only lists, not anything that subclasses lists. Either way, it's LBYL programming.
You might also wrap the append in a try... except block and catch TypeError exceptions, which would be more EAFP.

# 17.5 What is a special method attribute?

### Listing 17.1 File color_module.py
"""

# Listing 17.1 File color_module.py

class Color:
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue
    def __str__(self):
        return f"Color: R={self._red:d}, G={self._green:d}, B={self._blue:d}"

#from color_module import Color
c = Color(15, 35, 3)

print(c)

"""# 17.7 The `__getitem__` special method attribute

### Quick Check: __getitem__ The example use of __getitem__ above is very limited and won’t work correctly in many situations. What are some cases in which the implementation above will fail or work incorrectly?

#### Solution
This implementation will not work if you try to access an item directly by index; neither can you move backward.
"""

class LineReader:
    def __init__(self, filename):
        self.fileobject = open(filename, 'r')              #A
    def __getitem__(self, index):
        line = self.fileobject.readline()                  #B
        if line == "":                                #C
            self.fileobject.close()      #D
            raise IndexError         #E

        else:
            return line.split("::")[:2]                    #F

"""# 17.8 Giving an object full list capability"""

class TypedList:
    def __init__(self, example_element, initial_list=[]):
        self.type = type(example_element)                     #A
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must "
                          "be a list.")
        for element in initial_list:
                if not isinstance(element, self.type):
                    raise TypeError("Attempted to add an element of "
                                  "incorrect type to a typed list.")
        self.elements = initial_list[:]

class TypedList:
    def __init__(self, example_element, initial_list=[]):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must "
                            "be a list.")
        for element in initial_list:
            self.__check(element)
        self.elements = initial_list[:]
    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempted to add an element of "
                            "incorrect type to a typed list.")
    def __setitem__(self, i, element):
        self.__check(element)
        self.elements[i] = element
    def __getitem__(self, i):
        return self.elements[i]

x = TypedList("", 5 * [""])
x[2] = "Hello"
x[3] = "There"
print(x[2] + ' ' + x[3])

a, b, c, d, e = x
a, b, c, d

"""### Try This: Implementing list special methods
Try implementing the `__len__` and `__delitem__` special methods for TypedList, as well as an append method.
"""



# @title
class TypedList:
    def __init__(self, example_element, initial_list=[]):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must "
                            "be a list.")
        for element in initial_list:
            self.__check(element)
        self.elements = initial_list[:]
    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempted to add an element of "
                            "incorrect type to a typed list.")
    def __setitem__(self, i, element):
        self.__check(element)
        self.elements[i] = element
    def __getitem__(self, i):
        return self.elements[i]

    ################################
    ## SOLUTION
    ## added methods
    def __delitem__(self, i):
        del self.elements[i]
    def __len__(self):
        return len(self.elements)
    def append(self, element):
        self.__check(element)
        self.elements.append(element)

x = TypedList(1, [1,2,3])
print(len(x))
x.append(1)
del x[2]

"""## 17.9.1 Subclassing list"""

class TypedListList(list):
    def __init__(self, example_element, initial_list=[]):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must "
                            "be a list.")
        for element in initial_list:
            self.__check(element)
        super().__init__(initial_list)

    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempted to add an element of "
                            "incorrect type to a typed list.")

    def __setitem__(self, i, element):
        self.__check(element)
        super().__setitem__(i, element)

x = TypedListList("", 5 * [""])
x[2] = "Hello"
x[3] = "There"
print(x[2] + ' ' + x[3])

a, b, c, d, e = x
a, b, c, d

x[:]

del x[2]
x[:]

x.sort()
x[:]

"""## 17.9.2 Subclassing UserList"""

from collections import UserList
class TypedUserList(UserList):
    def __init__(self, example_element, initial_list=[]):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must "
                            "be a list.")
        for element in initial_list:
            self.__check(element)
        super().__init__(initial_list)

    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempted to add an element of "
                            "incorrect type to a typed list.")
    def __setitem__(self, i, element):
        self.__check(element)
        self.data[i] = element
    def __getitem__(self, i):
        return self.data[i]

x = TypedUserList("", 5 * [""])
x[2] = "Hello"
x[3] = "There"
print(x[2] + ' ' + x[3])

a, b, c, d, e = x
a, b, c, d

x[:]

del x[2]
x[:]

x.sort()
x[:]

"""### Quick Check: Special method attributes and subclassing  types

Suppose that you want a dictionary-like type that allows only strings as keys (maybe to make it work like a shelf object, as described in chapter 13). What options would you have for creating such a class? What would be the advantages and disadvantages of each option?

#### Solution

You could use the same approach as you did for `TypedList` and inherit from the `UserDict` class. You could also inherit directly from `dict`, or you could implement all of the `dict` functionality yourself.

Implementing everything yourself provides the most control but is the most work and most prone to bugs. If the changes you need to make are small (in this case, just checking the type before adding a key), it might make the most sense to inherit directly from `dict`. On the other hand, inheriting from `UserDict` is probably safest, because the internal `dict` object will continue to be a regular `dict`, which is a highly optimized and mature implementation.

# Lab 17: Creating a string only key:value dictionary

The quick check above mentions creating a dictionary that only allows strings as keys. Let's that idea a step further and actually implement a dictionary that only allows strings for both the keys and values. This sort of dictionary might be useful for example to cache URL's and web pages in a web application.

As mentioned in discussing lists above, you would have three possible approaches - write a class from scratch, inherit from the built-in dictionary, or inherit from UserDictionary. I would suggest for the best combination of simplicity and functionality that you inherit from the built-in `dict` type and override the  `__setitem__()` method.
"""

""" Create a dictionary that allows only strings for keys and values"""

class StringDict(dict):
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings') #A
        if not isinstance(value, str):
            raise TypeError('values must be strings')
        super().__setitem__(key, value)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        key_error = any(not isinstance(_, str) for _ in self.keys()) #B
        if key_error:
            raise TypeError('keys must be strings')
        value_error = any(not isinstance(_, str) for _ in self.values())
        if value_error:
            raise TypeError('values must be strings')

"""### Tests

These can be run after executing each cell which declares StringDict class.
"""

test_dict = StringDict()
test_dict['a'] = 'b'
test_dict['c'] = 'd'
print(test_dict)  # Output: {'a': 'b', 'c': 'd'}

test_dict = StringDict(a='b', c='d')
print(test_dict)  # Output: {'a': 'b', 'c': 'd'}

test_dict = StringDict([('a', 'b'), ('c', 'd')])
print(test_dict)  # Output: {'a': 'b', 'c': 'd'}

test_dict = StringDict()
test_dict['a'] = 1  # Raises TypeError: values must be strings
test_dict[2] = 'd'  # Raises TypeError: keys must be strings

test_dict = StringDict({a:1})  # Raises TypeError: values must be strings
test_dict = StringDict({2:'d'})  # Raises TypeError: keys must be strings

test_dict = StringDict([(1, 'b'), ('c', 'd')])  # Raises TypeError: keys must be strings
test_dict = StringDict([('a', 1), ('c', 'd')])  # Raises TypeError: values must be strings

"""### Copilot solution

Prompt:

```Create a subclass of dictionary that allows only strings as both keys and values.```
"""

class StringDict(dict):
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings')
        if not isinstance(value, str):
            raise TypeError('values must be strings')
        super().__setitem__(key, value)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.items():
            if not isinstance(key, str):
                raise TypeError('keys must be strings')
            if not isinstance(value, str):
                raise TypeError('values must be strings')

"""### Colaboratory solution

Prompt 1:

```Create a subclass of dictionary that allows only strings as both keys and values.```
"""

class StringDict(dict):
  def __setitem__(self, key, value):
    if not isinstance(key, str) or not isinstance(value, str):
      raise TypeError("Both keys and values must be strings.")
    super().__setitem__(key, value)

"""Prompt 1:

```Create a subclass of dictionary that allows only strings as both keys and values, including when creating the instance.```
"""

class StringDict(dict):
  def __init__(self, *args, **kwargs):
    super().__init__()
    for key, value in dict(*args, **kwargs).items():   #A
      self[key] = value      #B

  def __setitem__(self, key, value):
    if not isinstance(key, str) or not isinstance(value, str):
      raise TypeError("Both keys and values must be strings.")
    super().__setitem__(key, value)