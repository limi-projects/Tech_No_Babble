# Exceptions
Exceptions are objects that are used to handle errors.
If an exception is not addressed in the code, ```Python``` will provide a _traceback_, to report the location and nature of the error.

## Try-Except-else blocks 
These are used to handle exceptions. Put the bulk of your code in the ```try``` block, exceptions in the ```except``` block, and the desired outcome in the ```else``` block:
```python
def divider(n1,n2):
    try:
        outcome = n1/n2
    except ZeroDivisionError:
        print("Not allowed")
    else:
        print(outcome)

divider(3,2)
divider(2,0)
```
> 1.5\
> Not allowed

## Skipping errors
The pass statement can be used to ignore an error and move on.
```python
def divider(n1,n2):
    try:
        outcome = n1/n2
    except ZeroDivisionError:
        pass
    else:
        print(outcome)

divider(3,2)
divider(2,0)
```
> 1.5

## The ```raise``` keyword. 
