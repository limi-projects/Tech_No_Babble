# Figures

## ```plt.figures()```
Matplotlib's plot function can be used to generate a plot reliably. 
```python
import matplotlib.pyplot as plt
plt.plot([1,2],[4,5])
plt.show()
```
However, designating a ```figure``` object beforehand allows for more versatile manipulation of the plot.
```python
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes()
plt.plot([1,2],[4,5])
plt.show()
```
The gcf() and gca() methods allow a Figure and Axes object respectively to be manipulated. 

## Patches
Patches may be used to draw geometric shapes within a figure.
```python
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

circle = plt.Circle((0,0), radius = 0.5)
rectangle = plt.Rectangle((0,0), height=0.5, width=0.5)
ellipse = Ellipse((0,0), height=0.5, width=0.5)
triangle = plt.Polygon([(0,1), (1,1), (1,0)])

def make_shape(shape):
    ax = plt.gca()
    ax.add_patch(shape)
    plt.axis('scaled')
    plt.show()

make_shape(circle)
make_shape(rectangle)
make_shape(ellipse)
make_shape(triangle)
```

## Animations
Use the animation module to create animated figures.
```python
import matplotlib.pyplot as plt
from matplotlib import animation

circle = plt.Circle((0,0), radius = 0.5)

def _change_shape(i,shape):
    shape.radius = i*0.5
    return shape

def animate(shape):
    fig = plt.gcf()
    ax = plt.axes(xlim=(-10,10), ylim=(-10,10))
    ax.set_aspect('equal')
    ax.add_patch(shape)
    run = animation.FuncAnimation(
            fig, _change_shape, fargs=(shape,), frames=30, interval=50)
    plt.show()

animate(circle)
```
```fargs``` is the arguments that are to be passed to the _change_shape(shape,) helper function.
```frames``` is the number of animation frames.
```interval``` is the time gap between animations.

NB: Due to a quirk of matplotlib, the ```animation.FuncAnimation``` method must be assigned to a variable, even if that variable isn't callled. 
