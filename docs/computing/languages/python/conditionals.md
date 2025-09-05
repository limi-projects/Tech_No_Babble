# Conditional Statements
An ```if``` statement allows for a decision to be made, based on a predetermined set of True/False conditions.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]

for character in characters:
    if "t" in character:
        print(character)

# >> tinker
# >> tailor
# >> thief
```

## Non-numerical Comparisons
```python
if a in b: # If a is in b
if a not in b: # If a is not in b
a is b # If a is the same as b
a is not b # If a is not the same b
```

# Comparing Iterables
Iterables are compared numerically and alphabetically according to lexicographical ordering (See [here](https://docs.python.org/3/tutorial/datastructures.html) for further information).
```python
print((a, b) < (b, a)) # >> True
print((b, a) < (b, a)) # >> False
print((a, b) < (1, 2)) # >> False
print((b, a) < (1, 4)) # >> False
```

## Numerical Comparison Operators in if statements
```python
if a == b: # if a is equal to b.
if a != b: # if a is not equal to b.
if a < b: # if a is less than b
if a > b: # if a is more than b
if a >= b: # if a is more than or equal to b.
if a <= b: # if a is less than or equal to b.
```

## Multiple Conditions
Multiple conditions can be included in an if statement using ```and``` / ```or``` syntax.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]

for character in characters:
    if "t" in character and "e" in character:
        print(character)
# >> tinker
# >> thief
```

## If-Else Statements
```else``` may be used at the end of an if statement, to capture non-specific situations that do not meet the if statement condition.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
for character in characters:
    if "t" in character and "e" in character:
        print(character)
    else:
        print("Nothing")
# >> tinker
# >> Nothing
# >> Nothing
# >> Nothing
# >> Nothing
# >> Nothing
# >> Nothing
# >> thief
```
Note that ```else``` will not be executed if interrupted by ```break```, ```return```, or an error.

## If-Elif-Else Statements
```elif``` allows a further, specific scenario to be considered that does not meet the initial if statement condition.
Multiple ```elif``` statements may be included in an ```if-elif-else``` block.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
for character in characters:
    if "t" in character and "e" in character:
        print(character)
    elif "o" in character:
        print("Something")
    else:
        print("Nothing")
# >> tinker
# >> Something
# >> Something
# >> Something
# >> Nothing
# >> Something
# >> Nothing
# >> thief
```

Only one solution to ```if```, ```elif``` or ```else``` is permitted in a single ```if-elif-else``` block. Multiple ```if``` statements are necessary for <ins>separate and simultaneous</ins> conditions. This is because both conditions need to be satisfied in isolation.


#### [Back](README.md)
