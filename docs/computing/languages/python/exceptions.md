# Exceptions
Exceptions are objects that handle errors.

Without bespoke exception handling, ```Python``` will provide a defalult _traceback_, to report the error type and location.

## Try-Except-else blocks 
To handle exceptions yourself, put the bulk of the code in the ```try``` block, exceptions in the ```except``` block, and the desired outcome in the ```else``` block:
```python
def division_with_exception(dividend: int, divisor: int) -> float:
    '''Divides two integers. Throws a bespoke error if dividing by zero'''
    try:
         quotient = dividend/divisor
    except ZeroDivisionError:
        return("ERROR: You cannot divide by zero")
    else:
        return(quotient)

print(division_with_exception(3,2)) # >> 1.5
print(division_with_exception(2,0)) # >> ERROR: You cannot divide by zero
```

## Skipping errors
The pass statement can be used to ignore an error and move on.
```python
def division_skipping_exception(dividend: int, divisor: int) -> float:
    try:
         quotient = dividend/divisor
    except ZeroDivisionError:
        pass
    else:
        return(quotient)

print(division_skipping_exception(3,2)) # >> 1.5
print(division_skipping_exception(2,0)) # >> None
```

## The ```raise``` keyword. 
TODO
#### [Back](README.md)
