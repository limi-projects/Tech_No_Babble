# Automate the Boring Stuff with Python

## Pg 107 - Comma code
```python
def comma_code(lst):
    output = ', '.join(lst[:3]) + ' and ' + lst[-1]
    return output
comma_code(['a', 'b', 'c', 'd'])
```

## Pg 107 - Coin flip
```python
from random import choice

def coin_flip_streaks(n, search):
    #streaks = 0
    data = [choice(['H','T']) for i in range(n)]
    form = ''.join(data)
    print(form)
    occurences = form.count(search)
    print(occurences)

coin_flip_streaks(1000, 'TTTTTT')
```
## Pg 108 - Character Picture Grid
```python
from copy import copy # Needed to enusre that the nested lists are separate entities and not merely referencing the same entity.

empty = ' '
filled = 'o'
dimensions = (9, 6)
line = [empty] * dimensions[0]
lines =  [line.copy() for i in range(dimensions[1])] 

coords = ((2,3,5,6), (1,2,3,4,5,6,7), (1,2,3,4,5,6,7), (2,3,4,5,6), (3,4,5), (4,)) 

for y, x_vals in enumerate(coords):
    for x in x_vals:
        lines[y][x] = filled

for row in lines:
    print(''.join(row))
```

## Pg 120 - Noughts and crosses
