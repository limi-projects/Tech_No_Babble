## Cubic close packing
```python
from matplotlib import pyplot as plt

def ccp():
    '''Cubic close-packed crystal structure'''
    ax = plt.axes(xlim = (0,5), ylim = (0,5))
    square = plt.Rectangle((0,0), height=5, width=5)
    ax.add_patch(square)

    y = 0.5
    while y < 5:
        x = 0.5
        while x < 5:
            circle = plt.Circle((x,y), radius = 0.5, edgecolor='black')
            ax.add_patch(circle)
            x+=1.0
        y+=1.0
    plt.show()

ccp()
```

## Hexagonal close packing
```python
def hcp():
    '''Hexagonal close-packed crystal structure'''
    ax = plt.axes(xlim = (0,5), ylim = (0,5))
    square = plt.Rectangle((0,0), height=5, width=5)
    ax.add_patch(square)
    y1 = 0.5
    y2 = 0.5+0.5*(3)**0.5
    while y1 < 5 or y2 < 5:
        x1 = 0.5
        x2 = 1
        while x1 < 5 or x2 < 5:
            c1 = plt.Circle((x1, y1), radius = 0.5, edgecolor='black')
            c2 = plt.Circle((x2, y2), radius = 0.5, edgecolor='black')
            ax.add_patch(c1)
            ax.add_patch(c2)
            x1+=1
            x2+=1
        y1+=(0.5*(3)**0.5)*2
        y2+=(0.5*(3)**0.5)*2
    plt.show()

hcp()
```
