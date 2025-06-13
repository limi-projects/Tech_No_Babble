# The Collatz Conjecture
The Collatz Conjecture considers that for any integer that is > 1:
- if the number is even, divide it by two.
- if the number is odd, multpily it by 3 and add 1.

Continue to iterate on the output until 1 is reached.

Any number input to this sequence will, at some point, be equal to 1.

A proof for this relation is yet to be determined.

## Flowchart
```mermaid
---
config:
  theme: redux
  layout: dagre
---
flowchart TD
    A[/"Number"/] --> B["Print Number"]
    B --> C{"Number = 1?"}
    C -- Yes --> D(["Do nothing"])
    C -- No --> E{"Number is even?"}
    E -- Yes --> F["Number = Number/2"]
    E -- No --> H["Number = (3*Number)+1"]
    F --> A
    H --> A
```

## Python Code
```python
def collatz(number: int) -> int:
    ''' Collatz Sequence Generator

    Input an integer and the Collatz sequence will be printed.
    '''
    try:
        print(int(number))
        if number == 1:
            pass
        elif number % 2 == 0:
            number = number / 2
            collatz(number)
        else:
            number = (3 * number) + 1
            collatz(number)
    except ValueError:
        print('INVALID INPUT: ONLY INTEGERS ALLOWED')
```
