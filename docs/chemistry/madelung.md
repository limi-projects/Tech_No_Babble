# The Madelung Potential
<!--
ADD DESCRIPTION
-->


## Python Code
```python
from scipy.constants import pi, e, epsilon_0, N_A
from numpy import log
from limi_utils import plot_and_tabulate

one_dimensional_lattice = lambda z, d : (
        (-2 * N_A * log(2) * (z**2) * (e**2)) / 
        (4 * pi * epsilon_0 * d))

x_range = range(1, 11)

electronic_charges = [one_dimensional_lattice(i, 1) for i in x_range]
charge_separations = [one_dimensional_lattice(1, i) for i in x_range]

plot_and_tabulate(x_range, 
                  electronic_charges, 
                  'Electronic charge', 
                  'Electric potential')

plot_and_tabulate(x_range, 
                  charge_separations, 
                  'Charge separation', 
                  'Electric potential')
```

<!-- REFACTORED (Needs testing)
from math import pi, log

# Define constants.
PI, E, N_A, EPSILON_0 = pi, 1.602176634E-19, 6.02214076E-23, 8.8541878188E-12

def madelung_1D(z, d):
    '''Get the 1-D Madelung Potential for a given charge and interatomic distance.'''
    return (-2 * N_A * log(2) * (z**2) * (E**2)) / (4 * PI * EPSILON_0 * d)

print(madelung_1D(1,1))
-->