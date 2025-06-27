# Lists
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

#### [Back](../README.md)
