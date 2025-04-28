
## The ```math``` module


## Floor division
Ignores the remainder following a division operation.
```python
print(3//2)
```
> 1

## Fractions
Fraction objects can be created and manipulated.
```python
from fractions import Fraction
print(Fraction(1,2))
print(Fraction(3,4) + 5 + 2.7)
```
> 1/2
> 8.45

## Complex numbers
Use ```j``` instead of ```i``` to create and manipulate complex numbers.
```python
img1 = 1 + 1j
img2 = 2 - 3j
img3 = 4 + 0j
print(type(img1))
print(img1 - img2)
print(img3 / img1)
print(img1.real) # Get real value
print(img1.imag) # Get imaginary value
print(img1.conjugate()) # Get complex conjugate
print(abs(img2)) # Get the magnitude of the complex number
```
> <class 'complex'>
> (-1+4j)
> (2-2j)
> 1.0
> 1.0
> (1-1j)
> 3.605551275463989

NB: Cannot use floor division (```//```) or modulus (```%```) operations on complex numbers.
See ```cmath``` for further complex number operations.
