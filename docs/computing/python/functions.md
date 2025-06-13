# Functions
Functions allow you to save sections of code for repeated use. 
They are created using ```def``` and their output is controlled, using ```return```. 
Default arguments (parameters) are added in the preamble, using an ```=``` sign. 
Dcostrings are used to describe the function's purpose and usage.
```python
def transform(name=None): # Function to convert to list, then reverse
    """Transform a string"""
    match name:
        case None: # Return 'no name' if one isn't given
            return "No name"
        case name if type(name) != str: # Check that the input type is a string.
            return "Only string data types allowed!!"
        case _: # Otherwise, transform the string.
            transformed = list(name)
            transformed.reverse()
            return transformed

characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", ["thief"], ]

for char in characters:
    print(transform(char))

transform()
```
Output
```
['r', 'e', 'k', 'n', 'i', 't']
['r', 'o', 'l', 'i', 'a', 't']
['r', 'e', 'i', 'd', 'l', 'o', 's']
['r', 'o', 'l', 'i', 'a', 's']
['n', 'a', 'm', ' ', 'h', 'c', 'i', 'r']
['n', 'a', 'm', ' ', 'r', 'o', 'o', 'p']
['n', 'a', 'm', ' ', 'r', 'a', 'g', 'g', 'e', 'b']
Only string data types allowed!!
'No name'
```

Multiple arguments can be added to a function. Positional arguments are concise but opaque. 
Keyword arguments are clear but verbose. 
Default arguments are specified after non-default arguments. 
This ensures that the non-default arguments are picked up by the Python interpreter first.
```python
def shape(length = None, width = None, height = None):
    if length == None and width == None and height == None:
        return "Just a point"
    elif width == None and height == None:
        return "1D"
    elif height == None:
        return "2D"
    else:
        return "3D"

print(shape())
print(shape(length = 1))
print(shape(length = 1, width = 1))
print(shape(1, 1, 1))
```
Output
```
Just a point
1D
2D
3D
```

## Positional vs Keyword Arguments
Positional and keyword only argument formats may be forced using ```/``` and ```*``` respectively. 
Positional-only formats are useful for fucntions in which the keyword names are meaningless or misleading to the user.
Keyword-only formats are useful in the opposite scenario. 
```python
def shape(length = None, width = None, height = None, /):
    if length == None and width == None and height == None:
        return "Just a point"
    elif width == None and height == None:
        return "1D"
    elif height == None:
        return "2D"
    else:
        return "3D"

print(shape(1, 1, 1))
print(shape(length = 1, width = 1, height = 1))
```
Outputs
```
3D
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[4], line 12
      9         return "3D"
     11 print(shape(1, 1, 1))
---> 12 print(shape(length = 1, width = 1, height = 1))

TypeError: shape() got some positional-only arguments passed as keyword arguments: 'length, width, height'
```
Also
```python
def shape(*, length = None, width = None, height = None):
    if length == None and width == None and height == None:
        return "Just a point"
    elif width == None and height == None:
        return "1D"
    elif height == None:
        return "2D"
    else:
        return "3D"

print(shape(length = 1, width = 1, height = 1))
print(shape(1, 1, 1))
```
Outputs
```
3D
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[8], line 12
      9         return "3D"
     11 print(shape(length = 1, width = 1, height = 1))
---> 12 print(shape(1, 1, 1))

TypeError: shape() takes 0 positional arguments but 3 were given
```
Also
```python
def shape(length = None, /, width = None, *, height = None):
    if length == None and width == None and height == None:
        return "Just a point"
    elif width == None and height == None:
        return "1D"
    elif height == None:
        return "2D"
    else:
        return "3D"

print(shape(1, width = 1, height = 1))
print(shape(1, 1, height = 1))
print(shape(length = 1, width = 1, height = 1))
print(shape(1, 1, 1))
```
Outputs
```
3D
3D
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[10], line 13
     11 print(shape(1, width = 1, height = 1))
     12 print(shape(1, 1, height = 1))
---> 13 print(shape(length = 1, width = 1, height = 1))
     14 print(shape(1, 1, 1))

TypeError: shape() got some positional-only arguments passed as keyword arguments: 'length'
```

## Optional Arguments
Optional but known argumnets may be included by adding an empty keyword argument to the function defintion.
```python
def my_fn(name, age, weight=''):
    if weight:
        print(name, age, weight)
    else:
        print(name, age)

my_fn('Tom', 31)
my_fn('John', 42, 100)
```
Outputs
```
Tom 31
John 42 100
```
```end=''``` can be used within ```print()``` to remove the line break:
```python
print('a', end='')
print('b')
```
```
ab
```
 
## Arbitrary Arguments
The ```*args``` and ```**kwargs``` (or ```*``` and ```**```) tags may be used to account for additional aguments that may be input by the user (intentiaonlly or otherwise).
The additional arguments are stored in a tuple or dictionary that may be accessed via the ```*args``` and ```**kwargs``` variables within the function, respectively. 
If both are used within the same function, the ```*args``` must precede the ```**kwargs```.
This is useful if the arguments to be input into a function is not determined in advance.
Note also, that the ```*``` syntax is what matters, other names such as ```*stray_args``` or ```**stray_kwargs``` may also be used.
```*args``` and ```**kwargs``` must be specified after any known or default positional and keyword arguments.
```python
def cars(*args):
    return(args)

def car_uses(**kwargs):
    return(kwargs)

def car_mileage(*args,**kwargs):
    print(args)
    print(kwargs)

print(cars('toyota', 'renault', 'kia'))
print(car_uses(offroad = 'land rover', office = 'ford', shopping = 'toyota'))
car_mileage('toyota', 'renault', 'kia',  offroad = 'land rover', office = 'ford', shopping = 'toyota')
```
Outputs
```
('toyota', 'renault', 'kia')
{'offroad': 'land rover', 'office': 'ford', 'shopping': 'toyota'}
('toyota', 'renault', 'kia')
{'offroad': 'land rover', 'office': 'ford', 'shopping': 'toyota'}
```
A similar syntax can be used to very efficiently unpack iterables as arguments to a function.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
kw_characters = {
    "tinker" : 4,
    "tailor" : 8, 
    "soldier" : 15, 
    "sailor" : 16, 
    "rich man" : 23, 
    "poor man" : 42, 
    "beggar man" : 4, 
    "thief" : 8,
    }

def upk_chars(*args, **kwargs):
    print(args) 
    print(kwargs)

upk_chars(characters) # list treated as a single entry
upk_chars(kw_characters) # Dict treated as a single entry
upk_chars(*characters, **kw_characters) # List and dictionary unpacked into tuple and dictionary respectively
```
Outputs
```
(['tinker', 'tailor', 'soldier', 'sailor', 'rich man', 'poor man', 'beggar man', 'thief'],)
{}
({'tinker': 4, 'tailor': 8, 'soldier': 15, 'sailor': 16, 'rich man': 23, 'poor man': 42, 'beggar man': 4, 'thief': 8},)
{}
('tinker', 'tailor', 'soldier', 'sailor', 'rich man', 'poor man', 'beggar man', 'thief')
{'tinker': 4, 'tailor': 8, 'soldier': 15, 'sailor': 16, 'rich man': 23, 'poor man': 42, 'beggar man': 4, 'thief': 8}
```

## The ```return``` Statement
The ```return``` statement assigns an output to your function. This does not include printing the output. Thus, if it is desireable to do so, return statements can be printed by wrapping the called function in the ```print()``` statement. 
```python
def my_fn():
    return('hello')

# No print statement
my_fn()

# print via wrapping
print(my_fn())

# print via variable
output = my_fn()
print(output)
```
Outputs
```
hello
hello
```

## Lambda Expressions
These are anonymous (unnamed) functions and are a convenient way to represent simple functions with a single line of code.
```python
# Add two numbers together
add = lambda a, b : a + b
print(add(3,2))

# Add only odd numbers together
add_odd_only_list = lambda a, b : a + b if a % 2 != 0 and b % 2 != 0 else print('no odds')
print(add_odd_only(3,3))
print(add_odd_only(3,2))

# Add 5 to each element of a list, only if that element is odd, using a list comprehension.
# This results in lambda objects being created. 
# The values are accessed via "i()". 
add_odd_only_list = [lambda a=x : a+5 for x in range(0,10) if x % 2 != 0]
[print(i()) for i in add_odd_only_list]
```
Outputs
```
5
6
no odds
None
6
8
10
12
14
[None, None, None, None, None]
```

## Filter Function
The filter function accepts a function and a list of arguments. The filter fucntion will keep only the arguments that are returned by the function provided.
```python
# Keep only the characters with "t" in their names
# Note that a filter object is returned, which needs to be converted before printing.
characters = {"tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",}
accepted = filter(lambda x : 't' in x, characters)
print(set(accepted)) 
```
Outputs
```
{'thief', 'tinker', 'tailor'}
```

## Map Function
The map function applies a function to all elements of an iterable and will return the modified iterable.
```python
# Add "s" to each element of the set.
# Note that a filter object is returned, which needs to be converted before printing.
characters = {"tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",}
accepted = map(lambda x : x + 's', characters)
print(set(accepted)) 
```
Outputs
```
{'tinkers', 'rich mans', 'soldiers', 'tailors', 'beggar mans', 'poor mans', 'thiefs', 'sailors'}
```

## Local vs global variables.
Variables that are altered within a function are local to that function. 
Local variables cannot be accessed outside of the function unless a ```global``` statment is provided.
```python
def nonsense():
    gobbledigook = "bla, bla, bla"
    return None
print(gobbledigook)
```
Outputs a name error. However,
```python
gobbledigook = None

def nonsense():
    global gobbledigook
    gobbledigook = "bla, bla, bla"
    return None

print(gobbledigook) # variable hasn't been globally redefined yet.
print(nonsense()) # redefining the global variable
print(gobbledigook) # variable is globally redefined.
```
Outputs
```
None
None
bla, bla, bla
```
