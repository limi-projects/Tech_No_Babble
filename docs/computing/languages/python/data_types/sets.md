# Sets
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

## Set comprehensions
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

## Processing Sets
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

#### [Back](../README.md)
