# Regular Expressions

Regular expressions enable enhanced text searching and manipulation. 

The ```re``` module is required.

## Basic Searches
Use ```compile()``` to create _regex_ objects which can be used as templates for string searches using ```search()```. ```\d``` represents numeric digits. 

The output of ```search()``` is a _match_ object. The values of the match object can be extracted via the ```group()``` method.
```python
from re import compile, search

find_range = compile(r'\d-\d')
search_string = find_range.search('There are 4-5 people in this room')
print(search_string.group()) # >> 4-5
```

## Bracketing
The group function may be used to compartmentalise the regular expression. Each compartment may be called via a different ```group()``` index. Using the ```groups()``` method returns all compartments as a list.
```python
from re import compile, search

find_range = compile(r'(\d)-(\d)')
search_string = find_range.search('There are 4-5 people in this room')
print(search_string.group(0)) # >> 4-5
print(search_string.group(1)) # >> 4
print(search_string.group(2)) # >> 5
print(search_string.groups()) # >> ('4', '5')
```

## Escape characters
```\``` is an escape character which ignores a regex special character, such as a bracket.
```python
from re import compile, search

find_range = compile(r'(\(\d\))-(\d)')
search_string = find_range.search('There are (4)-5 people in this room')
print(search_string.group(0)) # >> (4)-5
print(search_string.groups()) # >> ('(4)', '5')
```

## Or Operations
OR operations can be ustilised using the ```|``` symbol. 

NB: only the first occurrence within a string gets picked up.

Enlcose ```|``` in parentheses to use it within substrings.
```python
from re import compile, search

f = compile(r'Tea (Bag|Cup|Party)')
s1 = f.search("Let's have a Tea Party")
print(s1.group(0)) # >> Tea Party
print(s1.group(1)) # >> Party
```

## Optional patterns
The ```?``` symbol enables optional pattern matching

```python
from re import compile, search

f = compile(r'(s)?he')
s1 = f.search("Is he available")
s2 = f.search("Is she available")
print(s1.group()) # >> he 
print(s2.group()) # >> she
```

## Repeating patterns patterns
The ```*``` symbol accounts for repetitions.
```python
from re import compile, search

f = compile(r'(s)*he')
s1 = f.search("Is he available")
s2 = f.search("Is sssssssssssshe available")
print(s1.group()) # >> he 
print(s2.group()) # >> sssssssssssshe
```

A specific number of repetitions can be required using ```{}```.
```python
from re import compile, search

f = compile(r'(a){5}')
s1 = f.search("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print(s1.group()) # >> aaaaa
```
A range of acceptable repeats can be specified by using ```{min,max}``` notation. 
```python
from re import compile, search

f = compile(r'(a){5,9}')
s1 = f.search("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print(s1.group(0)) # >> aaaaaaaaa
```
However, the maximum length match will always be prioritised over shorter matches (this is known as greedy matching). Non-greedy matching (i.e. the shortest match) can be prioritised using ```?``` 
```python
from re import compile, search

f = compile(r'(a){5}')
g = compile(r'a{5}')
s1 = f.findall("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
s2 = g.findall("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print(s1)# >> ['a', 'a', 'a', 'a', 'a', 'a']
print(s2)# >> ['aaaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaa']
```

## Finding All matches
The ```findall()``` method returns _all_ matching entries within a given string. 

NB: If groups (i.e. ```()```) are requested in ```compile()```, the code will behave slightly differently.
```python
from re import compile, search

f = compile(r'(a){5}')
g = compile(r'a{5}')
s1 = f.findall("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
s2 = g.findall("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print(s1)# >> ['a', 'a', 'a', 'a', 'a', 'a']
print(s2)# >> ['aaaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaa']
```

## Searching Character Classes
These are useful of you want to search based on the _data type_, rather than a specific value.
|Charater Class|Description|
|---|---|
|\d| A digit from 0-9|
|\D| A character (not 0-9)|
|\w| A letter, 0-9 or _|
|\W| A character (not a letter, 0-9 or _)|
|\s| A space, tab or newline character|
|\S| A character (not a space, tab or newline character)|

### Bespoke Character Classes
These can be specified using ```[]```. The ```^``` symbol can be used to reverse the search relationship. The ```-``` can be used to specify a range. 

NB: Escape charaters are not necessary inside square brackets
```python
from re import compile, search

f = compile(r'[a-e]')
g = compile(r'[^a-e]')
s1 = f.findall("Hello World")
s2 = g.findall("Hello World")
print(s1)# >> ['e', 'd']
print(s2)# >> ['H', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l']
```

## Searching String Ends
The ```^``` and ```$``` characters may be used to match patterns at the start and end of strings respectively.
```python
from re import compile, search

f = compile(r'^T')
g = compile(r'm$')
s1 = f.findall('There are 4-5 people in This room')
s2 = f.findall('there are 4-5 people in This rooM')
s3 = g.findall('There are 4-5 people in This room')
s4 = g.findall('there are 4-5 people in This rooM')
print(s1) # >> ['T']
print(s2) # >> []
print(s3) # >> ['m']
print(s4) # >> []
```

## Wildcard Searches
The ```.``` character will match any single character apart from a newline. Using ```.*``` will match all characters. Using ```re.DOTALL``` will include newline characters.

NB: The default matching is greedy. So use ```?``` where necessary for non-greedy matching.
```python
import re

f = re.compile(r'r.om')
g = re.compile(r'room')
h = re.compile(r'.*in')
i = re.compile(r'.*o.*')
j = re.compile(r'.*?o.*?')
k = re.compile(r'.*', re.DOTALL)
l = re.compile(r'.*')
s1 = f.findall('There are 4-5 people in This room')
s2 = g.findall('There are 4-5 people in This room')
s3 = h.findall('There are 4-5 people in This room')
s4 = i.findall('There are 4-5 people in This room')
s5 = j.findall('There are 4-5 people in This room')
s6 = k.findall('There are\n 4-5 people in This room')
s7 = l.findall('There are\n 4-5 people in This room')

print(s1) # >> ['room']
print(s2) # >> ['room']
print(s3) # >> ['There are 4-5 people in']
print(s4) # >> ['There are 4-5 people in This room']
print(s5) # >> ['There are 4-5 peo', 'ple in This ro', 'o']
print(s6) # >> ['There are\n 4-5 people in This room', '']
print(s7) # >> ['There are', '', ' 4-5 people in This room', '']
```

## Case Sensitivity
Case Sensitivity can be toggled by using ```re.IGNORECASE``` or ```re.I```.


#### [Back](README.md)
