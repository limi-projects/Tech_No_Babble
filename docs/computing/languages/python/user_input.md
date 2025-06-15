User input can be assigned to variables using the ```input()``` function.
```python
name = input("Enter your name: ")
print(f'Hello {name}')
```
Output
```
Enter your name: Limi
Hello Limi
```
Multiline greetings are also avialble
```python
intro = 'A script to repeat your name'
intro += '\nInsert name:'

name = input(intro)
print(f'Hello {name}')
```
Or you could use a docstring, but this may confuse the documentation
```
intro = '''A script to repeat your name
Insert name:'''

name = input(intro)
print(f'Hello {name}')
```
Output
```
A script to repeat your name
Insert name:Limi
Hello Limi
```
Note that the ```input()``` function returns strings. Any numerical inputs will have to be converted after passing through ```input()```.

## While Loops and ```input()```
While loops can be used to keep the input option available, for further commands, without closing the script.
```python
intro = 'A script to repeat your name'
intro += '\nInsert "close()" to shut this script down'
intro += '\nInsert name:'

name = ""
while name != 'close()':
    name = input(intro)

    if name != 'close()':
        print(f'Hello {name}\n')
```
Output
```
A script to repeat your name
Insert "close()" to shut this script down
Insert name:Tom
Hello Tom

A script to repeat your name
Insert "close()" to shut this script down
Insert name:Dick
Hello Dick

A script to repeat your name
Insert "close()" to shut this script down
Insert name:Harry
Hello Harry

A script to repeat your name
Insert "close()" to shut this script down
Insert name:close()
```

## _Flags_ can be used variables, to control the stat of the script.
```python
intro = 'A script to repeat your name'
intro += '\nInsert "close()" to shut this script down'
intro += '\nInsert name:'

active = True
while active:
    name = input(intro)

    if name == 'close()':
        active = False
    else:
        print(f'Hello {name}\n')
```
Outputs
```
A script to repeat your name
Insert "close()" to shut this script down
Insert name:Tom
Hello Tom

A script to repeat your name
Insert "close()" to shut this script down
Insert name:close()
```
#### [Back](README.md)
