from random import uniform
from math import pi

def estimate_pi(samples: int) -> float:  
    ''' Estimate the value of pi using a Monte Carlo simulation. '''  
    x = [uniform(0,1) for sample in range(samples)] # Get a uniform distribution of coordinates.
    y = [uniform(0,1) for sample in range(samples)]
    inside = sum(1 for x, y in zip(x, y) if x**2 + y**2 <= 1) # Count the number of coordinates inside the quadrant.
    estimate = (inside/samples)*4 
    return estimate

sample_densities = [1_00, 1_000, 1_000_0, 1_000_00, 1_000_000]
monte_carlo_runs = [estimate_pi(samples) for samples in sample_densities]
deviation_from_pi = list(map(lambda x : abs(x - pi), sample_densities))

print(sample_densities)
print(deviation_from_pi)

