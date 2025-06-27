# Numerical Data Types
## Integers
Integers do not contain decimal points.

### Arithmetic
```python
print(5 + 3) # Addtion 
print(5 - 3) # Subtraction
print(5 * 3) # Multiplication
print(5 / 3) # Division
print(5 % 3) # Modulo: Returns the remainder of a division operation
print(5 ** 3) # Indices
```
> 8\
> 2\
> 15\
> 1.6666666666666667\
> 2\
> 125

Negative numbers can be calculated directly. For instance, 
```python 
print(3 - 5)
```
> -2

#### Order of Operations
Keep in mind the rules of BIDMAS when performing arithmetic. If in doubt, use brackets to isolate arithmetic operations.
> Brackets\
> Indices\
> Division\
> Multiplication\
> Addition\
> Subtraction

## Floats
Floats are numbers that contain decimal points. They are named as such because
Division of two integers **always** results in a float.
An arithmetic operation between a float and an integer **always** results in a float.
Underscores may be used to manage the readability of large numbers (Python 3.6 and later).
```python
print(1_000_000.123_456_789)
```
> 1000000.123456789
