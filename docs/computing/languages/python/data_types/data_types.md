# Python Data Types

## Identifying and Converting Data Types
The ```type()``` function verifies the data type of a datum.
```python
print(type("String"))
print(type(1))
print(type(1.0))
print(type(["a", "b", "c"]))
print(type(("a", "b", "c")))
print(type({"a", "b", "c"}))
print(type({"a":1, "b":2, "c":3}))
```
> <class 'str'>\
> <class 'int'>\
> <class 'float'>\
> <class 'list'>\
> <class 'tuple'>\
> <class 'set'>\
> <class 'dict'>


## Strings
A string is a series of characters enclosed within quotation marks (" or ').
Strings are often used to represent text that is to be manipulated by the code.
```python
print("Hello")
print('Hello')
```
> Hello\
> Hello

Double quotation marks are recommended for general use as they allow for apostrophes to be enclosed within text.
Quotation marks can also be "escaped" using ```\```
```python
print('Isn\'t')
print("Isn't")
```
> Isn't\
> Isn't

### Manipulating Strings

#### Splitting
A string may be split into a list of strings by using the ```split()``` method.
```python
text = 'a b c'
split_string = text.split(' ')
print(split_string)
```
outputs
```
['a', 'b', 'c']
```

#### Capitalisation
The first word within a string may be capitalised via the ```title()``` method. 
```python
name = "the lord of the rings"
print(name)
print(name.title())
```
> the lord of the rings\
> The Lord Of The Rings

The entire string may be capitalised or decapitalised using the ```upper()``` and ```lower()``` methods, respectively.
```python
name = "The Lord of the Rings"
print(name)
print(name.upper())
print(name.lower())
```
> The Lord of the Rings\
> THE LORD OF THE RINGS\
> the lord of the rings

#### F-Strings
F-strings allow for data to be quickly formatted into strings. 
```python
name = "Apollo"
number = 11
shuttle = f"The {name} {number} space shuttle"
print(shuttle)
print(type(shuttle))
```
> The Apollo 11 space shuttle\
> <class 'str'>

As such, the integer assigned to the variable _"number"_ is converted into a string before adding it to the _"shuttle"_ variable.

Before version 3.6, Python used the ```format()``` method, which uses a different syntax.
```python
shuttle = "The {} {} space shuttle".format(name, number)
```

#### Spacing and Newlines
Use ```\t``` to add a tab space to a string. 
Use ```\n``` to add a new line to a string. 
Add ```\n``` at the end of a printed block, to make the output more readable.
Use the ```rstrip()```, ```lstrip()``` and ```strip()``` methods to strip whitespace from the right, left, and both sides of a string, respectively. 

```python
string = "           All work and no play makes Jack a dull boy\n\tAll work and no play makes Jack a dull boy\n         "
print(string)
print(string.rstrip())
print(string.lstrip())
print(string.strip())
```
```
            All work and no play makes Jack a dull boy
	All work and no play makes Jack a dull boy
         
           All work and no play makes Jack a dull boy
	All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
	All work and no play makes Jack a dull boy
         
All work and no play makes Jack a dull boy
 	All work and no play makes Jack a dull boy
```

Adding ```r``` before a quote allows an escape from the backslash character itself.
```python
print("\no")
print(r"\no")
```
```
	#Line Break
o
\no
```

## Integers
Integers do not contain decimal points.

### Arithmetic
```python
print(5 + 3) # Addtion 
print(5 - 3) # Subtraction
print(5 * 3) # Multiplication
print(5 / 3) # Division
print(5 % 3) # Modulo: Returns the remainder of a division operation
print(5 ** 3) # Indices
```
> 8\
> 2\
> 15\
> 1.6666666666666667\
> 2\
> 125

Negative numbers can be calculated directly. For instance, 
```python 
print(3 - 5)
```
> -2

#### Order of Operations
Keep in mind the rules of BIDMAS when performing arithmetic. If in doubt, use brackets to isolate arithmetic operations.
> Brackets\
> Indices\
> Division\
> Multiplication\
> Addition\
> Subtraction


## Floats
Floats are numbers that contain decimal points. They are named as such because
Division of two integers **always** results in a float.
An arithmetic operation between a float and an integer **always** results in a float.
Underscores may be used to manage the readability of large numbers (Python 3.6 and later).
```python
print(1_000_000.123_456_789)
```
> 1000000.123456789

## Lists
A list is an enumerated collection of items.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
print(characters)
```
### List Formatting
Line breaks can be included to make lists more readable. 
The final comma is usually unnecessary, but is included to make copy/paste operations quicker. 
For example, the formatting options below all result in the same list. 
```
characters = ["tinker", 
              "tailor", 
              "soldier", 
              "sailor", 
              "rich man", 
              "poor man", 
              "beggar man", 
              "thief",]

characters = [
    "tinker", 
    "tailor", 
    "soldier", 
    "sailor", 
    "rich man", 
    "poor man", 
    "beggar man", 
    "thief",
]

characters = [
    "tinker", 
    "tailor", 
    "soldier", 
    "sailor", 
    "rich man", 
    "poor man", 
    "beggar man", 
    "thief"
]
```

### List Indexing
List indexing starts at ```0```.
List indexing ends with ```-1```.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
print(characters[0])
print(characters[2])
print(characters[-1])
```
> tinker\
> soldier\
> thief

The index of a given item may also be found with the ```index()``` method.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
print(characters.index("soldier"))
```
results in ```2```.
The ```count()``` method will return the number of times a particular value appears in a list.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
print(characters.count("tailor"))
```
> 1

### List Slicing
A subset of a list (a _slice_) may be extracted from a list using ```<list>[<start>:<end>]``` syntax.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
print(characters[2:4]) # only elements 2 and 3.
print(characters[:4]) # all elements up to (and including) the fourth. 
print(characters[5:]) # all elements after the fifth.
print(characters[-5:]) # all elements after (and including) the fifth, counting backwards.
print(characters[:-5]) # all elements before (and not including) the fifth, counting backwards.
print(characters[:6:2]) # all elements up to (and not including) the sixth, in increments of 2.
print(characters[:]) # copy list (all entries)
```
> ['soldier', 'sailor']\
> ['tinker', 'tailor', 'soldier', 'sailor']\
> ['poor man', 'beggar man', 'thief']\
> ['sailor', 'rich man', 'poor man', 'beggar man', 'thief']\
> ['tinker', 'tailor', 'soldier']\
> ['tinker', 'soldier', 'rich man']\
> ['tinker', 'tailor', 'soldier', 'sailor', 'rich man', 'poor man', 'beggar man', 'thief']

Lists can be copied using the ```copy()``` method.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
duplicate = characters.copy()
print(characters)
print(duplicate)
```
> ['tinker', 'tailor', 'soldier', 'sailor', 'rich man', 'poor man', 'beggar man', 'thief']\
> ['tinker', 'tailor', 'soldier', 'sailor', 'rich man', 'poor man', 'beggar man', 'thief']

### List Manipulation - Adding Elements
List elements may be redefined according to the appropriate index.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
characters[1] = "spy"
print(characters)
```
Elements may be added to the end of the list using the ```append()``` and ```extend()```method.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
characters.append('doctor')
characters.extend(["doctor", "lawyer", "indian chief"])
print(characters)
```
> ['tinker', 'tailor', 'soldier', 'sailor', 'rich man', 'poor man', 'beggar man', 'thief', 'doctor', 'doctor', 'lawyer', 'indian chief']

Elements may be inserted into the list at the desired index using the ```insert()``` method.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
characters.insert(2,'lawyer')
print(characters)
```
> ['tinker', 'tailor', 'lawyer', 'soldier', 'sailor', 'rich man', 'poor man', 'beggar man', 'thief']

### List Manipulation - Removing Elements
Elements may be removed using ```del```. 
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
del characters[3]
del characters[5:7]
print(characters)
```
> ['tinker', 'tailor', 'soldier', 'rich man', 'poor man']

The entire list can be emptied by using the ```clear()``` method.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
characters.clear()
print(characters)
```
> []

The ```pop()``` method allows you to remove and retain list elements.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
removed_character = characters.pop(2)
print(characters)
print(removed_character)
```
> ['tinker', 'tailor', 'sailor', 'rich man', 'poor man', 'beggar man', 'thief']\
> soldier

Elements are removed according to the **first instance** of their value via the ```remove()``` method.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
characters.remove("tailor")
print(characters)
```
> ['tinker', 'soldier', 'sailor', 'rich man', 'poor man', 'beggar man', 'thief']

### List Manipulation - Sorting Elements
Elements may be **permanently** sorted alphabetically or numerically using the ```sort()``` method.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",] # Alphabetical
numbers = [4, 8, 15, 16, 23, 42] # Numerical
characters.sort()
numbers.sort(reverse=True) # Sorting in reverse order this time, merely to demonstrate.
print(characters)
print(numbers)
```
> ['beggar man', 'poor man', 'rich man', 'sailor', 'soldier', 'tailor', 'thief', 'tinker']\
> [42, 23, 16, 15, 8, 4]

Elements may be **temporarily** sorted alphabetically or numerically using the ```sorted()``` method.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
numbers = [4, 8, 15, 16, 23, 42]
print(sorted(characters))
print(sorted(numbers))
```
> ['beggar man', 'poor man', 'rich man', 'sailor', 'soldier', 'tailor', 'thief', 'tinker']\
> [4, 8, 15, 16, 23, 42]

Elements may be listed **permanently** in reverse order using the ```reverse()``` method.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",] 
characters.reverse()
print(characters)
```
> ['thief', 'beggar man', 'poor man', 'rich man', 'sailor', 'soldier', 'tailor', 'tinker']

### List Analysis - Length
The length of a list may be found using the ```len()``` function.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",] 
print(len(characters))
```
> 8

### List Analysis - Comparing Two Lists
Two lists may be compared using for loops and conditional statements.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
check_for = ["tinker", "tailor", "poor man", "beggar man",]

for char in check_for:
    if char in characters:
        print(characters.index(char))
```
> 0\
> 1\
> 5\
> 6

### Numerical List Analysis
The ```sum()```, ```min()``` and ```max()``` functions may be used to calculate the sum, minimum and maximum values from a list, respectively.
```python
print(sum(range(1, 10, 1)))
print(min(range(1, 10, 1)))
print(max(range(1, 10, 1)))
```
> 45\
> 1\
> 9

## Numerical List Creation
The ```range()``` function generates a numerical list within a given range and set of increments.
However, the range data type must first be converted into a list using the ```list()``` function.
```python
print(list(range(-10, 10, 2)))
```
> [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8]

The result does not include the end value specified in the range function.

### List Comprehensions
List comprehensions may be used instead of a for loop to create one list from another.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
t_characters = [ele for ele in characters if "t" in ele]
print(t_characters)
```
> ['tinker', 'tailor', 'thief']

## Tuples
Tuples are _immutable_ lists. Immutable means that the values within cannot be changed.
Tuples are defined using parentheses. 
Only the <ins>entire</ins> tuple can be redefined via a variable. Individual elements within the tuple cannot be redefined.
```python
characters = ("tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",)
print(characters)
characters = ("doctor", "lawyer", "indian chief")
print(characters)
```
> ('tinker', 'tailor', 'soldier', 'sailor', 'rich man', 'poor man', 'beggar man', 'thief')\
> ('doctor', 'lawyer', 'indian chief')

## Sets
A set is an unordered list of elements that contains no repeats. 
It is a collection of distinct elements, wherein no two set elements are the same.
The number of members in the set is the cardinality.
This is useful when duplicates are to be avoided and the ordering of the elements is irrelevant.
A set may be defined via braces, with no key-value pairs.
```python
characters = {"tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",}
print(characters)
```
> {'poor man', 'tinker', 'tailor', 'rich man', 'soldier', 'sailor', 'beggar man', 'thief'}

### Set comprehensions
Set comprehensions may be used to streamline set generation
```python
characters = {"tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",}

t_s = {char for char in characters if "t" in char} 
print(t_s)
```
> {'thief', 'tinker', 'tailor'}

The ```set()``` function converts other data types to a set. This is useful if you only want unique entries to be mentioned.
```python
characters = {
    "tinker" : 4,
    "tailor" : 8, 
    "soldier" : 15, 
    "sailor" : 16, 
    "rich man" : 23, 
    "poor man" : 42, 
    "beggar man" : 4, 
    "thief" : 8,
    "thief" : 8,
    "rich man" : 23,
    }
for key in set(characters.keys()):
    print(f"{key}")
```
> poor man\
> tinker\
> tailor\
> rich man\
> soldier\
> sailor\
> beggar man\
> thief

### Processing Sets
Sets can be further manipulated using the ```FiniteSet()``` class of ```sympy```
```python
from sympy import FiniteSet
a = FiniteSet(1,2)
b = FiniteSet(1,2,3)
# To see is one set is a SUBset of another.
print(a.is_subset(b))
# To see is one set is a SUPERset of another.
print(b.issuperset(a))
# Get all possible subsets.
print(a.powerset())
# To see is one set is a proper SUBset of another.
print(a.is_proper_subset(b))
# Get the union (all unique values) across two sets.
print(a.union(b))
# Get the intersection (all common values) across two sets.
print(a.intersect(b))
# Get the cartesian product (all possible pairs) across two sets.
[print(i) for i in a*b]
# Get the cartesian product (all possible triplets) across three sets.
[print(i) for i in a**3]
```
> True\
> True\
> FiniteSet(EmptySet, {1}, {2}, {1, 2})\
> True\
> {1, 2, 3}\
> {1, 2}\
> (1, 1)\
> (2, 1)\
> (1, 2)\
> (2, 2)\
> (1, 3)\
> (2, 3)\
> (1, 1, 1)\
> (2, 1, 1)\
> (1, 2, 1)\
> (2, 2, 1)\
> (1, 1, 2)\
> (2, 1, 2)\
> (1, 2, 2)\
> (2, 2, 2)

## Dictionaries
Instead of numeric indexes (like lists), dictionaries use _"keys"_ to manage _"values"_.
Dictionaries are defined using ```{key:value, key:value, ...}``` syntax.
```python
characters = {
    "tinker" : 4,
    "tailor" : 8, 
    "soldier" : 15, 
    "sailor" : 16, 
    "rich man" : 23, 
    "poor man" : 42, 
    "beggar man" : 4, 
    "thief" : 8,
    }
print(characters)
print(characters["tinker"])
```
> {'tinker': 4, 'tailor': 8, 'soldier': 15, 'sailor': 16, 'rich man': 23, 'poor man': 42, 'beggar man': 4, 'thief': 8}\
> 4

New key-value pairs may be added and altered using ```<dict>[<key>] = <value>``` syntax. Key-value pairs may be removed with the ```del <dict>[<key>]``` syntax.
```python
characters = {
    "tinker" : 4,
    "tailor" : 8, 
    "soldier" : 15, 
    "sailor" : 16, 
    "rich man" : 23, 
    "poor man" : 42, 
    "beggar man" : 4, 
    "thief" : 8,
    }
characters["doctor"] = 15
characters["tinker"] = 23
characters["sailor"] += 9 # Add 9 to original value.
del characters ["poor man"]
print(characters)
```
> {'tinker': 23, 'tailor': 8, 'soldier': 15, 'sailor': 25, 'rich man': 23, 'beggar man': 4, 'thief': 8, 'doctor': 15}

Dictionaries store different information pieces about one object (e.g. a single person's height, weight, etc.) or the same piece of information for many objects (e.g. the heights of many people).

### The ```get()``` method
The ```get()``` method allows you to search for keys within a dictionary, and if the key isn't present, a fallback value can be provided.
```python
stuff = {'a':5, 'b':9}
print(stuff.get('a', 'Missing'))
print(stuff.get('c', 'Missing'))
```
```
5
Missing
```

### The ```setdefault()```  method
This method sets a default value for a key-value pair. The value cannot be changed once this is done.
```python
stuff = {'a':5, 'b':9}
stuff.setdefault('def', 'unchanged')
print(stuff)
stuff.setdefault('def', 'changed')
print(stuff)
stuff['def'] = 'changed'
print(stuff)
```
```
{'a': 5, 'b': 9, 'def': 'unchanged'}
{'a': 5, 'b': 9, 'def': 'unchanged'}
{'a': 5, 'b': 9, 'def': 'changed'}
```

### Looping through dictionaries
Looping through keys, values or both is controlled via the ```keys()```, ```values()``` and ```items()``` methods.
If unspecified, the dictionary will only loop through its keys.
```python
characters = {
    "tinker" : 4,
    "tailor" : 8, 
    "soldier" : 15, 
    "sailor" : 16, 
    "rich man" : 23, 
    "poor man" : 42, 
    "beggar man" : 4, 
    "thief" : 8,
    }
for key, value in characters.items():
    print(f"{key} {value}")
```
> tinker 4\
> tailor 8\
> soldier 15\
> sailor 16\
> rich man 23\
> poor man 42\
> beggar man 4\
> thief 8

```python
characters = {
    "tinker" : 4,
    "tailor" : 8, 
    "soldier" : 15, 
    "sailor" : 16, 
    "rich man" : 23, 
    "poor man" : 42, 
    "beggar man" : 4, 
    "thief" : 8,
    }
for key in characters.keys():
    print(f"{key}")
```
> tinker\
> tailor\
> soldier\
> sailor\
> rich man\
> poor man\
> beggar man\
> thief

```python
characters = {
    "tinker" : 4,
    "tailor" : 8, 
    "soldier" : 15, 
    "sailor" : 16, 
    "rich man" : 23, 
    "poor man" : 42, 
    "beggar man" : 4, 
    "thief" : 8,
    }
for value in characters.values():
    print(f"{value}")
```
> 4\
> 8\
> 15\
> 16\
> 23\
> 42\
> 4\
> 8
```
### Dictionary Comprehensions
Dictionary comprehensions may be used to streamline the coding of simple loops.
```python
characters = {
    "tinker" : 4,
    "tailor" : 8, 
    "soldier" : 15, 
    "sailor" : 16, 
    "rich man" : 23, 
    "poor man" : 42, 
    "beggar man" : 4, 
    "thief" : 8,
    }

t_characters = {key:value*2 for key, value in characters.items() if "t" in key} # Copies "t" containing keys from the characters dictionary, multilies the value by 2, and puts them in the t_characters dictionary.
print(t_characters)
```
> {'tinker': 8, 'tailor': 16, 'thief': 16}

#### [Back](README.md)
