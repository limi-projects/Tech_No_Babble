# Strings
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

## Raw Strings
Adding ```r``` before a quote allows an escape from the backslash character itself.
```python
print("\no")
print(r"\no")
```
```
o #Line Break
\no
```

## Indexing and Slicing
Like lists, strings can be sliced.
```python
greeting = 'hello'
print(greeting[0], greeting[0:3],)
```
```
h hel
```

## Inspecting contents

```in``` and ```not in``` can be used to search the contents of strings.
```python
'i' in 'hello'
```
```
False
```

| Method | Result | Description
|---|---|---|
| 'hello'.isalpha() | True | True if string is not blank and only contains letters
| 'hello'.isalnum() | True | True if string is not blank and only contains letters and numbers
| 'hello'.isdecimal() | False | True if string is not blank and only contains numbers
| 'hello'.isspace() | False | True if string is not blank and only contains spaces, tabs, newlines.
| 'hello'.istitle() | False | True if words begin with capital letters and follow with lowercase letters.
| 'hello'.startswith('h') | True | True if string begins with a chosen substring.
| 'hello'.endswith('o') | True | True if string ends with a chosen substring.

## Splitting & Joining
A string may be split into a list or tuple of strings by using the ```split()``` or ```partition()``` methods resepctively.
```python
text = 'a b c'
split_string_1 = text.split(' ')
split_string_2 = text.partition(' b ')
print(split_string_1)
print(split_string_2)
```
outputs
```
['a', 'b', 'c']
('a', ' b ', 'c')
```

Coversely, a list may be joined into one string via the ```join()``` method.
```python
text = ['a', 'b', 'c']
joined_list = ' '.join(text)
print(joined_list)
```
```
a b c
```

## Capitalisation
The first word within a string may be capitalised via the ```title()``` method. 
```python
name = "the lord of the rings"
print(name)
print(name.title())
```
> the lord of the rings\
> The Lord Of The Rings

The entire string may be capitalised or decapitalised using the ```upper()``` and ```lower()``` methods respectively. 
```python
name = "The Lord of the Rings"
print(name)
print(name.upper())
print(name.lower())
```
```
The Lord of the Rings
THE LORD OF THE RINGS
the lord of the rings
```

## F-Strings
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

Before version 3.6, Python used the ```format()``` or ```%s %s``` method , which uses a different syntax.
```python
shuttle = "The {} {} space shuttle".format(name, number)
shuttle = "The %s %s space shuttle" % (name, number)
```

## Spacing and Newlines
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

## Padding
String padding can be modified using ```rjust()```, ```ljust()``` and ```center()```.
```python
print('tinker'.rjust(10,'='))
print('tailor'.ljust(10,'='))
print('soldier'.center(11,'='))
```
```
====tinker
tailor====
==soldier==
```

## Stripping Whitespace
Whitespace can be stripped using ```strip()```, ```rstrip()```, and ```lstrip()```.
```python
print('    tinker      '.strip())
print('    tailor'.lstrip())
print('    soldier      '.rstrip())
```
```
tinker
tailor
    soldier
```

## Multiline Strings
These also act as annotations within functions and classes.
```python
print(
    '''
    Line 1
    Line 2
    Line 3
    ''')
```
```
    Line 1
    Line 2
    Line 3
```

## Unicode values
The Unicode value of a character or the character of a Unicode value cand be obtained using the ```ord()``` and ```chr()``` functions.
```python
print(ord('a'))
print(chr(97))
```
```
97
a
```

#### [Back](../README.md)
