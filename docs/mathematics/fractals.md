## Barnsley Fern
```python
import random
import matplotlib.pyplot as plt
from sympy import sympify

transformations = [
        ('0.85*x + 0.04*y', '-0.04*x + 0.85*y + 1.6', 0.85),
        ('0.2*x - 0.26*y', '0.23*x + 0.22*y + 1.6', 0.07),
        ('-0.15*x + 0.28*y', '-0.26*x + 0.24*y + 0.44', 0.07),
        ('0', '0.85*y', 0.01),]

def get_index(probability):
    r = random.random()
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    for item, sp in enumerate(sum_probability):
        if r <= sp:
            return item
    return len(probability)-1

def transform(p, transformations):
    probabilities = [t[2] for t in transformations]
    tindex = get_index(probabilities)
    t = transformations[tindex]
    x = sympify(t[0]).subs({'x': p[0],'y': p[1]})
    y = sympify(t[1]).subs({'x': p[0],'y': p[1]})
    return x, y

def draw(n, transformations):
    x, y = [0], [0]
    x1, y1 = 0, 0
    for i in range(n):
        x1, y1 = transform((x1, y1), transformations)
        x.append(x1)

x,y = draw(1000, transformations)
plt.plot(x, y, 'o')
plt.show()
```
