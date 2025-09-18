# Loops
Loops enable iteration of a given task over multiple entries.

## For loops
For loops iterate across a set number of entries. Often elements within a list.
They use the 
```python
for <element> in <iterable>:
  <do task>
```
syntax, until all of the elements within the iterable have been processed. For example:
```python
for ele in ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]:
    print(ele)

'''Outputs'''
tinker
tailor
soldier
sailor
rich man
poor man
beggar man
thief
```
A for loop will cycle sequentially, until all entries are exhausted, **before** allowing the next line of code to run. 
Operations that are inside or outside of the loop are controlled via indentation.
```python
for ele in ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]:
    print(ele)
print("doctor")

'''Outputs'''
tinker
tailor
soldier
sailor
rich man
poor man
beggar man
thief
doctor
```
To avoid confusion and bugs, it is recommended to use a relevant and descriptive name for the temporary (```<ele>```) variable that is used in a for loop.

## While Loops
A while loop will execute its contents, as long as its condition remains true. 
They should be used with caution, to avoid infinitely repeating sequences that must be manually broken.
```python
x = 0
while x < 10:
    print(x)
    x += 1
```
Output
```
0
1
2
3
4
5
6
7
8
9
```
They should be used, instead of for loops, to modify iterables. This is because while loops are better atkeeping track of the items in the list.
```python
from time import sleep

train_1 = ['passenger1', 'passenger2', 'passenger3',]
train_2 = []

while train_1:
    alighting = train_1.pop()
    print(f'{alighting} is alighting...')
    sleep(10)
    train_2.append(alighting)
    print(f'currently boarded: {train_2}')
```
Outputs
```
passenger3 is alighting...
currently boarded: ['passenger3']
passenger2 is alighting...
currently boarded: ['passenger3', 'passenger2']
passenger1 is alighting...
currently boarded: ['passenger3', 'passenger2', 'passenger1']
```
Removing items using a while loop.
```python
train = ['passenger1', 'passenger2', 'passenger3',]

while 'passenger2' in train:
    train.remove('passenger2')

print(train)
```
Outputs
```
['passenger1', 'passenger3']
```
Adding items using a while loop.
```python
train = ['passenger1', 'passenger2', 'passenger3',]

at_stop = True

print('At the station')
while at_stop:

    leaving = input('Leaving: ')
    if leaving == 'departing':
        break
    else:
        train.remove(leaving)

    boarding = input('Boarding: ')
    if boarding == 'departing':
        break
    else:
        train.append(boarding)

print(f'On train: {train}')
```
Outputs
```
At the station
Leaving: passenger3
Boarding: Limi
Leaving: departing
On train: ['passenger1', 'passenger2', 'Limi']
```

## Break statements
Break statements allow you terminate from a given innermost loop. Note that no furhter code will be executed, once the break statement is reached.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
for title in characters:
    if title == "rich man":
        break # Kill this loop at rich man
    else:
        for letter in title:
            if letter == "a":
                break # Kill this loop at the first letter "a" that's encountered.
            else:
                print(letter)
```
Output
```
t
i
n
k
e
r
t
s
o
l
d
i
e
r
s
```
Alternatively, ```sys.exit()``` can also be used to exit the entire program, regardless of the program's progress.
## Continue Statements
Continue statements allow you move onto the next iteration of a loop, whilst taking an alternative action. This is good for exceptional cases within an iterable. 
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]
for title in characters:
    if title == "rich man":
        continue
    print(title)
```
Output (note also 8, not 9, elements in total because of the continue statement)
```
tinker
tailor
soldier
sailor
poor man
beggar man
thief
```

## Pass Statements
Pass statements do nothing and are often used as placeholders within classes and functions, allowing sections of code to be avoided until they are ready to be worked on.
```python
def to_do_list():
    pass # print some stuff before.
    print("stuff")
    pass # Print some more stuff later.
to_do_list()
```

```
stuff
```

## Match Statements
Match staments are used to compare data. Very usefulfor handling errors and deadline with systematic comparisons.
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]

def outcasts(message):
    match message:
        case "thief":
            print("Away with you!")
        case "beggar man":
            print("Away with you!")
        case _: # Wildcard, to include all other possibilities.
            print("Welcome!")

for char in characters:
    outcasts(char)
```
or
```python
characters = ["tinker", "tailor", "soldier", "sailor", "rich man", "poor man", "beggar man", "thief",]

def outcasts(message):
    match message:
        case "thief" | "beggar man":
            return("Away with you!")
        case _: # Wildcard, to include all other possibilities.
            return("Welcome!")

for char in characters:
    print(outcasts(char))
```
Output
```
Welcome!
Welcome!
Welcome!
Welcome!
Welcome!
Welcome!
Away with you!
Away with you!
```
Can also perform several matches, using tuples
```python
def shape(length = None, width = None, height = None, ):
    match (length, width, height):
        case (None, None, None):
            return("0D")
        case (length, None, None):
            return("1D")
        case (length, width, None):
            return("2D")
        case (length, width, height):
            return("3D")
        case _:
            return("Invalid Entry")

print(shape()) # No argument give.
print(shape(length = 1)) # 1 keyword argument given
print(shape(length = 1, width = 1)) # 2 keyword arguments given
print(shape(1, 1, 1)) # 3 positional arguments given
```
Outputs
```
0D
1D
2D
3D
```
#### [Back](README.md)
