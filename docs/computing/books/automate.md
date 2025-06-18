```python
def comma_code(lst):
    output = ', '.join(lst[:3]) + ' and ' + lst[-1]
    return output
comma_code(['a', 'b', 'c', 'd'])
```

```python
from random import choice

def coin_flip_streaks(n, search):
    streaks = 0
    data = [choice(['H','T']) for i in range(n)]
    form = ''.join(data)
    print(form)
    if search in form:
        print('Y')

coin_flip_streaks(1000, 'TTTTTT')
```
