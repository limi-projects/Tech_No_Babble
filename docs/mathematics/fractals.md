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

## Sierpinski Triangle
```python
import random
import matplotlib.pyplot as plt
from sympy import sympify

transformations = [
        ('0.5*x', '0.5*y', 0.33),
        ('0.5*x + 0.5', '0.5*y + 0.5', 0.33),
        ('0.5*x + 1', '0.5*y', 0.33),]

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
        y.append(y1)
    return x,y

x,y = draw(1000, transformations)
plt.plot(x, y, 'o')
plt.show()
```

## Henon's function
```python
import random
import matplotlib.pyplot as plt
from sympy import sympify

transformations = [('y + 1 - 1.4*(x**2)', '0.3*x', 0.33),]

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
    x1, y1 = 1, 1
    for i in range(n):
        x1, y1 = transform((x1, y1), transformations)
        x.append(x1)
        y.append(y1)
    return x,y

x,y = draw(1000, transformations)
plt.plot(x, y, 'o')
plt.show()
```

## Mandelbrot Set
```python
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

def initialise_image(x_p, y_p):
    image = []
    for i in range(y_p):
        x_colours = []
        for j in range(x_p):
            x_colours.append(0)
        image.append(x_colours)
    return image

def colour_points():
    n = 400
    max_iteration = 1000
    x0, x1 = -2.5, 1
    y0, y1 = -1, 1
    image = initialise_image(n,n)
    dx = (x1-x0)/(n-1)
    dy = (y1-y0)/(n-1)
    x_coords = [x0 + i*dx for i in range(n)]
    y_coords = [y0 + i*dy for i in range(n)]
    for i,x in enumerate(x_coords):
        for k,y in enumerate(y_coords):
            z = complex(0,0)
            c = complex(x,y)
            iteration = 0
            while abs(z) < 2 and iteration < max_iteration:
                z = (z**2) + c
                iteration+=1
            image[k][i] = iteration
    plt.imshow(image, origin='lower', extent=(-2.5, 1, -1, 1),
               cmap=cm.Greys_r, interpolation='nearest')
    plt.show()

colour_points()
```
