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
