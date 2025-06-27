# Dictionaries
Instead of numeric indexes (like lists), dictionaries use _"keys"_ to manage _"values"_.
Dictionaries are mutable.
The elements within a dictionary are not ordered. Consequently, they cannot be sliced.
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

## The ```get()``` method
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

## The ```setdefault()```  method
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

## Looping through dictionaries
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
