# Comments

## Standard Comments
Use ```#``` to add single-line comments. 
```python
# This is a comment.
print("Bla, Bla, Bla.")
```
Outputs
```
Bla, Bla, Bla.
```

## Docstrings
Use ```""" """``` to add documentation strings (docstrings).
Docstrings should be used to describe modules, functions and classes. 
These descriptions can be accessed by calling the ```__doc__``` attribute.

The recommended format is as follows:
```python
def some_fn():
    """What the function does.

    Other noteworthy comments about the function.
    """
    pass

print(some_fn.__doc__)
```
Outputs
```
What the function does.

    Other noteworthy comments about the function.
```

## Annotations
These allow you to specify the function's input/output data types.
```python
def some_fn(param1 : str, param2 : int) -> float:
    pass

print(some_fn.__annotations__)
```
Outputs
```
{'param1': <class 'str'>, 'param2': <class 'int'>, 'return': <class 'float'>}
```
