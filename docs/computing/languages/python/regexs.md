```python
import re

# \d for digits
regex = re.compile(r'\d\d\d-\d\d\d\d')
string = regex.search('Search number 0203040404-040404 333')
print(string.group())
```
```
404-0404
```

```python
import re

# Use bracketing to break up the regular expression.
regex = re.compile(r'(\d\d\d)-(\d\d\d\d)')
string = regex.search('Search number 0203040404-040404 333')
print(string.group())
print(string.group(0))
print(string.group(1))
print(string.group(2))
```
```
404-0404
404-0404
404
0404
```

```python
import re

# \ is an escape character.
regex = re.compile(r'\((\d\d\d\))-(\d\d\d\d)')
string = regex.search('Search number 0203040(404)-040404 333')
print(string.group())
print(string.group(0))
print(string.group(1))
print(string.group(2))
```
```
(404)-0404
(404)-0404
404)
0404
```

```python
import re

# | as an or operator. NB: Only the first encountered value is picked up.
regex = re.compile(r'020|333')
string1 = regex.search('Search number 0203040(404)-040404 333')
string2 = regex.search('Search number 333 0203040(404)-040404')
print(string1.group())
print(string2.group())
```
```
020
333
```

```python
import re

# | in brackets to parse substrings.
regex = re.compile(r'Tea (bag|cup|party)')
string = regex.search('Tea bag')
print(string.group())
print(string.group(1))
```
```
Tea bag
bag
```

```python
import re

# use ()? to add optional substrings.
# Use ()* to count all occurrences of optional substrings.
# Use ()+ to count all instances of a substring.
regex = re.compile(r'-\d\d\d\d\d\d( \d\d\d)?')
string1 = regex.search('Search number 0203040(404)-040404')
string2 = regex.search('Search number 0203040(404)-040404 333')
print(string1.group())
print(string2.group())

regex = re.compile(r'-\d\d\d\d\d\d( \d\d\d)*')
string3 = regex.search('Search number 0203040(404)-040404 333 333 333')
print(string3.group())

regex = re.compile(r'-\d\d\d\d\d\d( \d\d\d)+') # Will fail if no instances exist.
string4 = regex.search('Search number 0203040(404)-040404 333 333 333')
print(string4.group())
```
```
-040404
-040404 333
-040404 333 333 333
-040404 333 333 333
```

```python
import re

# Use (){} to make repeated text searches more concise.
regex = re.compile(r'(5){9}')
string = regex.search('555555555555555555555')
print(string.group())
```
```
555555555
```

#### [Back](README.md)
