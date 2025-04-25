# Classes
A ```Class``` represents a thing or situation. 
```Objects``` are created from classes. 
Each object is a version of the class, with unique variations.
```Instantiation``` is creating an object from a class.
Hence, objects are often referred to as ```instances``` of a class. 
Classes are defined using *CamelCase*, whilst instances are defined using *underscores_and_lowercase*.
A ```method``` is a function that is part of a class.
The ```__init__()``` syntax ensures that Python does not confuse your class's methods with those of default methods.
The ```self``` syntax ensures that every method call associated with an instance automatically passes ```self```.

```python
class ChemicalElement:
    '''Defining the attributes of a chemical element.'''
    
    def __init__(self, name, protons, neutrons,):
        '''Initialise the attributes of the class.'''
        self.name = name
        self.protons = protons
        self.neutrons = neutrons
        self.discovery_date = '[EMPTY]'

    def get_details(self):
        '''Display the details of the element.'''
        details = f'\nName: {self.name}\nNumber of Protons: {self.protons}\nNumber of Neutrons: {self.neutrons}'
        return details

    def get_mass(self):
        '''Get the atomic mass.'''
        proton_mass = 1.6726*pow(10,-27)
        neutron_mass = 1.6749*pow(10,-27)
        mass = (self.protons*proton_mass) + (self.neutrons*neutron_mass)
        return mass

H = ChemicalElement('Hydrogen', 1, 0)
N = ChemicalElement('Nitrogen', 7, 7)

print(H.get_details()) # Execute function and print output.
print(H.get_mass()) # Execute another function and print output.
print(N.get_mass())
print(H.discovery_date) # Print the default value of an attribute
H.discovery_date = 1766 # Redefine an attribute
print(H.discovery_date)
```
> Name: Hydrogen\
> Number of Protons: 1\
> Number of Neutrons: 0\
> 1.6726e-27\
> 2.34325e-26\
> [EMPTY]\
> 1766

## Inheritance
Inheritance allows you to generate a class from a similar parent class. 
To do this, the new class must refer to the old class, i.e. ```class NewClass(OldClass)```. 
The ```super()``` method may be used within the Child classes ```__init__``` function, to inherit the parent class's methods.
```python
# Parent Class
class ChemicalElement:
    '''Defining the attributes of a chemical element.'''
    
    def __init__(self, name, protons, neutrons):
        '''Initialise the attributes of the class.'''
        self.name = name
        self.protons = protons
        self.neutrons = neutrons
        self.discovery_date = '[EMPTY]'

    def get_details(self):
        '''Display the details of the element.'''
        details = f'\nName: {self.name}\nNumber of Protons: {self.protons}\nNumber of Neutrons: {self.neutrons}'
        return details

    def get_mass(self):
        '''Get the atomic mass.'''
        proton_mass = 1.6726*pow(10,-27)
        neutron_mass = 1.6749*pow(10,-27)
        mass = (self.protons*proton_mass) + (self.neutrons*neutron_mass)
        return mass

H = ChemicalElement('Hydrogen', 1, 0)
print(f'H protons: {H.protons}')
print(f'H neutrons: {H.neutrons}')

# Child Class
class ChemicalIsotope(ChemicalElement):
    '''Defining the attributes of a Chemical isotope.'''

    def __init__(self, name, protons, neutrons):
        '''Initialise the attributes of the child class.'''
        super().__init__(name, protons, neutrons)

D = ChemicalIsotope('Deuterium', 1, 1)
print(f'D protons: {D.protons}')
print(f'D neutrons: {D.neutrons}')
print(D.get_mass())
```
> H protons: 1\
> H neutrons: 0\
> D protons: 1\
> D neutrons: 1\
> 3.3475e-27

Methods may also be redefined within a child class to accommodate further changes to the class.
```python
# Parent Class
class ChemicalElement:
    '''Defining the attributes of a chemical element.'''
    
    def __init__(self, name, protons, neutrons):
        '''Initialise the attributes of the class.'''
        self.name = name
        self.protons = protons
        self.neutrons = neutrons
        self.discovery_date = '[EMPTY]'

    def get_details(self):
        '''Display the details of the element.'''
        details = f'\nElement Name: {self.name}\nNumber of Protons: {self.protons}\nNumber of Neutrons: {self.neutrons}'
        return details

    def get_mass(self):
        '''Get the atomic mass.'''
        proton_mass = 1.6726*pow(10,-27)
        neutron_mass = 1.6749*pow(10,-27)
        mass = (self.protons*proton_mass) + (self.neutrons*neutron_mass)
        return mass

# Child Class
class ChemicalIsotope(ChemicalElement):
    '''Defining the attributes of a Chemical isotope.'''

    def __init__(self, name, protons, neutrons):
        '''Initialise the attributes of the child class.'''
        super().__init__(name, protons, neutrons)

    def get_details(self):
        '''Display the details of the isotope.'''
        details = f'\nIsotope Name: {self.name}\nNumber of Protons: {self.protons}\nNumber of Neutrons: {self.neutrons}'
        return details

H = ChemicalElement('Hydrogen', 1, 0)
D = ChemicalIsotope('Deuterium', 1, 1)

print(H.get_details())
print(D.get_details())
```
> Element Name: Hydrogen\
> Number of Protons: 1\
> Number of Neutrons: 0

> Isotope Name: Deuterium\
> Number of Protons: 1\
> Number of Neutrons: 1

An instance of a class can also be used as an attribute for another class, without any prior inheritance steps. This is useful for combining multiple classes as components in a greater object.
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
        '''Initialise the attributes of the class.'''
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

#### Back to [Python](../README.md) | [Computing](../../README.md) | [Home](../../../README.md)
