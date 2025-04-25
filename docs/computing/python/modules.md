# Modules
Modules allow you to store your functions, in separate files, for later use. 
This allow you to keep your python scripts relatively short and modular; thereby making the overall structure of the code easier to understand.
Modules may be imported using the ```import``` syntax.
Aliases for modules may also be used, using the ```as``` syntax, for conciseness.
Furthermore, particular functions from a given module may be imported, for further 
Python already has large libraries of useful modules, such as ```numpy```.
```python
import numpy
data = numpy.linspace(1,10,10)
data2 = numpy.array([1,2,3])
print(data)
print(data2)
```
or
```python
import numpy as np
data = np.linspace(1,10,10)
data2 = np.array([1,2,3])
print(data)
print(data2)
```
or
```python
from numpy import linspace as lsp, array
data = lsp(1,10,10)
data2 = array([1,2,3])
print(data)
print(data2)
```
All result in the same outputs
```
[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
[1 2 3]
```

Note also that the difference between ```from numpy import *``` and ```import numpy``` is that when ```*``` is used, the module (numpy) does not need to be specified using dot notation (i.e. numpy.array), when calling the function.
However, using the ```*``` method is not recommended, as it often leads to bugs in the program.

## Importing classes
Clases may be imported by calling their respective name
```python
# Attribute Class
class ElectronicStructure:
    '''Defining the attribute class.'''

    def __init__(self, electrons):
        self.electrons = electrons

    def elec_strt(self):
        return 'Electronic structure 1s orbital'

# Class
class ChemicalElement:
    '''Defining the attributes of a chemical element.'''
    
    def __init__(self, name, protons, neutrons):
        '''Intitialise the attributes of the class.'''
        self.name = name
        self.protons = protons
        self.neutrons = neutrons
        self.discovery_date = '[EMPTY]'
        self.electrons = ElectronicStructure(protons) # Assigning attribute class

    def get_details(self):
        '''Display the details of the ELEMENT.'''
        details = f'\nElement Name: {self.name}\nNumber of Protons: {self.protons}\nNumber of Neutrons: {self.neutrons}'
        return details

    def get_mass(self):
        '''Get the atomic mass.'''
        proton_mass = 1.6726*pow(10,-27)
        neutron_mass = 1.6749*pow(10,-27)
        mass = (self.protons*proton_mass) + (self.neutrons*neutron_mass)
        return mass

H = ChemicalElement('Hydrogen', 1, 0)

print(H.get_details())
print(H.electrons.electrons)
print(H.electrons.elec_strt())
```
Improting the above ChemicalElement class, in a file called test_class.py, is done via
```python
from test_class import ChemicalElement

H = ChemicalElement('Hydrogen', 1, 0)
print(H.get_details())
```
Or
```python
import test_class

H = test_class.ChemicalElement('Hydrogen', 1, 0)
print(H.get_details())
```
Outputs
```
Element Name: Hydrogen
Number of Protons: 1
Number of Neutrons: 0
```
