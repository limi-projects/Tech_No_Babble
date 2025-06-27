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

## Manipulating Strings

### Splitting
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

### Capitalisation
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

### F-Strings
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

### Spacing and Newlines
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

#### [Back](../README.md)
