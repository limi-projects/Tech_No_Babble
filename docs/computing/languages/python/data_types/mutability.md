# Mutabilityq
Mutable data types can be edited on the fly. 
For example, a list's elements can be added, removed or replaced. 
Therefore, a list is <ins>mutable</ins>.

String or tuple elements cannot be added, removed or replaced.
Hence, they are <ins>immutable</ins>.

## References

When a variable is assigned a value, that variable references the value in the computer's memory.
Thus, variable values only truly change when they are assigned to new values.
```python
a = 1
b = a
a = 2
print(a,b)
```
```
2 1
```
The reason ```b``` is not equalt to 2 is because it was assigned to the value 1, via ```a```, and was not reassigned. 
```a``` was reassigned to a new value. 

However, this does not apply to list elements because list elements are merely references to the same values in the computer's memory.
Thus, when list elements are reassigned, they do apply to each instance of the list. 
```python
a = [1]
b = a
a[0] = 2
print(a,b)
```
```
[2] [2]
```
Therefore, caution should be used when reassigning variables and elements.

### The ```id()``` method
The ```id()``` function can be used to test referencing in Python.
```python
a = [1]
b = a
a[0] = 2
print(a,b)
print(id(a),id(b))
```
```
[2] [2]
35804320 35804320
```
```python
a = 1
b = a
a = 2
print(a,b)
print(id(a),id(b))
```
```
2 1
3250180 3250164
```
Note that the *automatic garbage collector* deletes unused values to free up memory.

### The ```copy()``` and ```deepcopy()``` methods.
These create copies of mutable data, not just references.
Use ```copy()``` for list and ```deepcopy()``` for lists of lists.
```python
import copy

# List
a = [1]
b = copy.copy(a)

# Nested list
c = [[1]]
d = copy.deepcopy(c)

print(id(a),id(b))
print(id(c[0]),id(d[0]))
```
```
40592256 40592856
40592432 40591968
```

