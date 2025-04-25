# Testing

An automated suite of tests can be put together, to ensure that the code works properly.
For example, create a class (ChemicalElement) and store it in a file (t_class):
```python
class ChemicalElement:
    '''Defining the attributes of a chemical element.'''

    def __init__(self, name, protons, neutrons,):
        '''Intitialise the attributes of the class.'''
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
```
Then create a suite of tests, in a separate file, using the ```unittest``` module.

```python
import unittest
from t_class import ChemicalElement

class TestChemicalElement(unittest.TestCase):
    '''Tests for the ChemicalElement class.'''

    def setUp(self):
        '''Create a set of test case inputs for all situations.'''
        self.H_pass = ChemicalElement('Hydrogen', 1, 0) # This should PASS
        self.H_fail = ChemicalElement('Hydrogen', 'One', 0) # This should FAIL

    def test_get_mass_pass(self):
        '''Test the get_mass function.

        Compare the actual output with the expected output.
        This should PASS.
        '''
        self.assertEqual(self.H_pass.get_mass(), 1.6726e-27)

    def test_get_mass_fail(self):
        '''Test the get_mass function again, with a different input.

        This should FAIL.
        '''
        self.assertEqual(self.H_fail.get_mass(), 1.6726e-27)

# Initiates testing of all "test_" labelled fucntions.
if __name__ == '__main__':
    unittest.main()
```
Running the above script outputs:
```
E.
======================================================================
ERROR: test_get_mass_fail (__main__.TestChemicalElement.test_get_mass_fail)
Test the get_mass function.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/limi/test.py", line 26, in test_get_mass_fail
    self.assertEqual(self.H_fail.get_mass(), 1.6726e-27)
                     ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/limi/t_class.py", line 20, in get_mass
    mass = (self.protons*proton_mass) + (self.neutrons*neutron_mass)
            ~~~~~~~~~~~~^~~~~~~~~~~~
TypeError: can't multiply sequence by non-int of type 'float'

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (errors=1)
```
```E``` means that a test has failed, as mentioned in the above script.
```.``` means that a test has passed, as mentioend in the above script.

There are futher comparion operators for testing, including:
- assertEqual(a, b)
- assertNotEqual(a, b)
- assertTrue(bool)
- assertFalse(bool)
- assertIn(item, iterable)
- assertNotIn(item, iterable)
