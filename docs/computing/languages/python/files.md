## Reading Files
Files can be read and stored into memory, in their entireity, or read line by line.
In the below case, the contents of the file are stored as an object.
```python
with open('test.txt') as file:
    contents = file.read()
print(contents)
```
> hello

"test.txt" can be replaced with a _relative_ file path (i.e. "files/test.txt") or an _absolute_ file path, if the e is stored in another directory.
Note also that windows systems use backslashes to declare file paths. However, this should not affect the way the code is interpreted.

## Reading line-by-line
```python
with open('test.txt') as file:
    for line in file:
        print(line.rstrip()) #rstrip to remove added whitespace, leading to blank lines.
```
> hello\
> bonjour\
> guten tag

If it is desireable to save the files lines, outside the ```with``` block, as a list ```readlines()``` may be used.
```python
with open('test.txt') as file:
    lines = file.readlines()

print(lines[0].rstrip())
```
> hello

Note that all file data is read as a string. As such, numerical data will need to be converted after it is read.
```python
with open('test.txt', 'w') as file:
    file.write('goodbye')
    file.write('\nAu revoir')

with open('test.txt') as file:
    contents = file.read()
print(contents)
```
> goodbye\
> Au revoir

Note that 'w' stands for write, 'r' stands for read, and 'a' stands for append. Writing to an existing file will erase its contents; only adding the new contents.  
Appending allows new content to be written to the end of the file.
```python
with open('test.txt', 'a') as file:
    file.write('\nguten morgen')

with open('test.txt') as file:
    contents = file.read()
print(contents)
```
> goodbye\
> Au revoir\
> guten morgen\
> guten morgen

## The JSON module
Stands for Javascript Object Notation.
Allows data to be stored in a coding language insensitive format.
```python
import json

data = ['a', 'b', 'c']

name = 'data.json'
with open(name, 'w') as f:
    json.dump(data, f)
```
then
```python
import json

name = 'data.json'
with open(name) as f:
    stuff = json.load(f)

print(stuff)
```
> ['a', 'b', 'c']

## Using JSON as a database file
```python
''' Check if a key is in the database json file.

Optional: If not, it can be added.
'''

import json

file = 'data.json' # Contains: {"Tom": "metadata", "Dick": "metadata", "Harry": "metadata"}
data = input('Check database: ')

with open(file, 'r') as read_file:
    database = json.load(read_file)

if data in database:
    print(f'{data} is in the database')
else:
    print(f'{data} is not in the database')
    prompt = input('Add data (y/n)\n')
    if prompt == 'y':
        database.update({data : "metadata"})
        with open(file, 'w') as write_file:
            json.dump(database, write_file)
    elif prompt == 'n':
        quit()
    else:
        print("Input not recognised")
```

## The ```shutil``` module
The ```shutil``` module is a means to manipulate files.
TO DO

## The ```csv``` module
The ```csv``` module is a means to manipulate ```.csv``` files.
TO DO
#### [Back](README.md)
