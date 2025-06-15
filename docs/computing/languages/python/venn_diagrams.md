# Venn diagrams
These may be ploteed using ```matplotlib-venn```.
```python
from matplotlib_venn import venn2
import matplotlib.pyplot as plt

a = {1,3,5,7,9}
b = {2,3,5,6,11}
venn2(subsets=[a,b])
plt.show()
```
#### [Back](README.md)
