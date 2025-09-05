# Classes
A ```Class``` represents an entity or scenario. 

## Definitions
- **_Objects_** are created from classes. Each object is a version of the class, with unique variations.
- **_Instantiation_** involves creating an object from a class. Hence, objects are often referred to as ```instances``` of a class. 
- **_PascalCase_** (aka Upper Camel Case) is used to define classes (i.e. ```class ThisIsAClass:```)
- **_snake_case_** (```def this_is_an_instance():```).
- **_Methods_** are functions of a class.
- ```__init__()``` ensures that Python does not confuse your class's methods with ```Python```'s default methods.
- ```self``` ensures that every method call associated with an instance automatically passes ```self```.
- **_Inheritance_** allows you to generate a class from a parent class. The new class must refer to the old class (i.e. ```class NewClass(OldClass)```). 

## Class Example
Here is an example of a class for a chemical element.
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

print(H.get_details()) # >> Name: Hydrogen
                       # >> Number of Protons: 1
                       # >> Number of Neutrons: 0
print(H.get_mass()) # >> 1.6726e-27
print(N.get_mass()) # >> 2.34325e-26
print(H.discovery_date) # >> [EMPTY]
H.discovery_date = 1766
print(H.discovery_date) # >> 1766
```

## Inheritance Example
The ```super()``` method may be used within the child classes ```__init__``` function, to inherit the parent class's methods.
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
print(f'H protons: {H.protons}') # >> H protons: 1
print(f'H neutrons: {H.neutrons}') # >> H neutrons: 0

# Child Class
class ChemicalIsotope(ChemicalElement):
    '''Defining the attributes of a Chemical isotope.'''

    def __init__(self, name, protons, neutrons):
        '''Initialise the attributes of the child class.'''
        super().__init__(name, protons, neutrons)

D = ChemicalIsotope('Deuterium', 1, 1)
print(f'D protons: {D.protons}') # >> D protons: 1
print(f'D neutrons: {D.neutrons}') # >> D neutrons: 1
print(D.get_mass()) #>> 3.3475e-27
```

## Redefining Inherited Methods
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

print(H.get_details()) # >> Element Name: Hydrogen
                       # >> Number of Protons: 1
                       # >> Number of Neutrons: 0
print(D.get_details()) # >> Isotope Name: Deuterium
                       # >> Number of Protons: 1
                       # >> Number of Neutrons: 1
```

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

print(H.get_details()) # >> Element Name: Hydrogen
                       # >> Number of Protons: 1
                       # >> Number of Neutrons: 0
print(H.electrons.electrons) # >> 1
print(H.electrons.elec_strt()) # >> Electronic structure 1s orbital
```

#### Back to [Python](./README.md) | [Computing](../README.md) | [Home](../../README.md)
#### [Back](README.md)
