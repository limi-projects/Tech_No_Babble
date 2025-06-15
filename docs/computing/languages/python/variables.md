# Variables
Variables are used to label peices of information to be re-used and/or redefined in the code.
Each _variable_ represents an associated _value_.

## Variable Naming Guidelines
Variable names should:
- only contain letters, numbers, or underscores;
- not start with a number;
- not start with an uppercase letter;
- not use existing Python keywords, such as ```print```;
- not be excessively long;
- be descriptive.
Interpretation of the above is somewhat subjective. 

## Usage
Varaibles are defined via the syntax _"variable = value"_. 
```python
greeting = "Hello"
```

### Defining Multiple variables
Multiple variables may be defined across a single line using commas ```,``` 
```python
greeting, farewell = "Hello", "Goodbye"
```
or line-by-line.
```python
greeting = "Hello"
farewell = "Goodbye"
```

## Redefining Variables
Variables may be redefined, by using the same _"variable = value"_ syntax, at a later point in the code.
```python
greeting = "Hello"
greeting = "Good day"
```

## Constants
Constants are defined by caplialising the vairable name.
```python
PLANCK_CST = 6.626e-34
```
#### [Back](README.md)
