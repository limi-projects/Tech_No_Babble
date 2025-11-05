# Monte Carlo Simulations

Monte Carlo simulations use (pseudo)random selection to aproach an accurate solution. 
Since the sampling is randomised, the accuracy of a Monte Carlo simulation increases with the number of samples, at the cost of an increased computational load.

## Demonstration$
The value of ${\pi}$ may be estimated using a Monte Carlo simulation. 

1. Consider a circle with a radius of ${r}$, bounded by a square.
   The ratio of the area of the circle and the area of the square is:
   ${\frac{\pi r^{2}}{4r^{2}} = \frac{\pi}{4}}$.
2. Symmetry reduce the problem to a quadrant, enclosed by a smaller square of width r.
   The ${\frac{\pi}{4}}$ ratio still holds in this configuration.
4. Consider that the circle and square are centred about an origin (0,0) and that ${r=1}.
5. Sample randomly within this space, recording the coordinates.
6. Via the Pythagorean theorem (${a^{2} + b^{2} = c^{2}}$).
   Samples that have a disance from the origin of less than, or equal to, 1 must be within the quadrant.
   Categorise each sample accordingly.
7. Divide the number of samples within the quadrant by the total number of samples.
   This is effectively producing the same circle/square division calculation, as above,
   albeit using pointwise sampling of the area.
8. Multiply the result by 4, to estimate ${\pi}$.

The estimation improves as the number of samples is increased, at the cost of an increased duration of the calculation.

```python
from random import uniform

def estimate_pi(samples: int) -> float:  
    ''' Estimate the value of pi using a Monte Carlo simulation. '''  
    x = [uniform(0,1) for sample in range(samples)] # Get a uniform distribution of coordinates.
    y = [uniform(0,1) for sample in range(samples)]
    inside = sum(1 for x, y in zip(x, y) if x**2 + y**2 <= 1) # Count the number of coordinates inside the quadrant.
    estimate = (inside/samples)*4 
```