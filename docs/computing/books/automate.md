# Automate the Boring Stuff with Python

## Pg 107 - Comma code
```python
def comma_code(lst):
    output = ', '.join(lst[:3]) + ' and ' + lst[-1]
    return output
comma_code(['a', 'b', 'c', 'd'])
```

## Pg 107 - Coin flip
```python
from random import choice

def coin_flip_streaks(n, search):
    #streaks = 0
    data = [choice(['H','T']) for i in range(n)]
    form = ''.join(data)
    print(form)
    occurences = form.count(search)
    print(occurences)

coin_flip_streaks(1000, 'TTTTTT')
```
## Pg 108 - Character Picture Grid
```python
from copy import copy # Needed to enusre that the nested lists are separate entities and not merely referencing the same entity.

empty = ' '
filled = 'o'
dimensions = (9, 6)
line = [empty] * dimensions[0]
lines =  [line.copy() for i in range(dimensions[1])] 

coords = ((2,3,5,6), (1,2,3,4,5,6,7), (1,2,3,4,5,6,7), (2,3,4,5,6), (3,4,5), (4,)) 

for y, x_vals in enumerate(coords):
    for x in x_vals:
        lines[y][x] = filled

for row in lines:
    print(''.join(row))
```

## Pg 120 - Noughts and crosses
```python
nnc_board = {'TL': ' ', 'TM': ' ', 'TR': ' ',
             'ML': ' ', 'MM': ' ', 'MR': ' ',
             'LL': ' ', 'LM': ' ', 'LR': ' ',}

def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['LL'] + '|' + board['LM'] + '|' + board['LR'])

def play_noughts_and_crosses():
    turn = 'X'
    for i in range(9):
        print_board(nnc_board)
        print(f"{turn}'s turn.")
        move = input()
        nnc_board[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'    

play_noughts_and_crosses()
```

## Pg 127 - Chessboard
```python
chessboard = {'1h': 'bP', '7a': 'wQ', '9z': 'Iv'}

rows = ['1', '2', '3', '4', '5', '6', '7', '8', ]
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ]
colours = ['b','w']
roles = ['P', 'R', 'N', 'B', 'K', 'Q', ]

def check_field(item, field):
    if item in field:
        pass
    else:
        print(f'Error: {item} is an invalid index')

for place, piece in chessboard.items():
    row, column, colour, role = place[0], place[1], piece[0], piece[1] 
    check_field(row, rows)
    check_field(column, columns)
    check_field(colour, colours)
    check_field(role, roles)
```

### Extra: Build chessboard

```python
from copy import copy

def translate(l):
    for k, v in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ]):
        if l == v:
            return k
            
p = {
    'wR1': ['a', 1], 'wN1': ['b', 1], 'wB1': ['c', 1], 'wK ': ['d', 1], 'wQ ': ['e', 1], 'wB2': ['f', 1], 'wN2': ['g', 1], 'wR2': ['h', 1],
    'wP1': ['a', 2], 'wP2': ['b', 2], 'wP3': ['c', 2], 'wP4': ['d', 2], 'wP5': ['e', 2], 'wP6': ['f', 2], 'wP7': ['g', 2], 'wP8': ['h', 2], 
    'bP1': ['a', 7], 'bP2': ['b', 7], 'bP3': ['c', 7], 'bP4': ['d', 7], 'bP5': ['e', 7], 'bP6': ['f', 7], 'bP7': ['g', 7], 'bP8': ['h', 7],
    'bR1': ['a', 8], 'bN1': ['b', 8], 'bB1': ['c', 8], 'bK ': ['d', 8], 'bQ ': ['e', 8], 'bB2': ['f', 8], 'bN2': ['g', 8], 'bR2': ['h', 8],
     }

empty, filled = '   ', 'o'
dimensions = (8, 8)
line = [empty] * dimensions[0]
lines =  [line.copy() for i in range(dimensions[1])] 
print('   ', ' '.join([' a ', ' b ', ' c ', ' d ', ' e ', ' f ', ' g ', ' h ', ]))
print('_' * 35)

for k, v in p.items():
    lines[v[1]-1][translate(v[0])] = k

for row, line in enumerate(lines, 1):
    print('  |')
    print(row, '|', ' '.join(line))

print('  |')
```

## Pg 127 - Game inventory
```python
inventory = {'arrow': 12, 'gold': 42, 'rope': 1, 'torch': 6, 'dagger': 1}
loot = {'gold': 10, 'rope': 1, 'ruby': 1}

def display_inventory(inventory):
    print('Inventory:')
    for k, v in inventory.items():
        print(v, k)
    print(f'Total items: {sum(inventory.values())}')

def add_to_inventory(inventory, additions):
    for k, v in additions.items():
        if k in inventory.keys():
            inventory[k] += v
        else:
            inventory[k] = v

add_to_inventory(inventory, loot)
display_inventory(inventory)
```

## Pg 144 - Multiclipboard Automatic Messages
Create reusable, modifiable text that can be copied to the clipboard.
```python
from pyperclip import copy, paste
from sys import argv

def assign_result(result : str) -> str:
    '''Identify the pass/fail verdict.'''
    match result.lower():
        case 'pass' | 'passed' | 'p':
            return "I'm pleased to report that this matter has Passed Testing"
        case 'fail' | 'failed' | 'f':
            return "Unfortunately, this matter has Failed Testing.\n\nIn short:"
        case _:
            return 'ERROR: INVALID RESULT VALUE'

def assign_recipient(recipient : str) -> str:
    '''Identify the recipient.'''
    match recipient.lower():
        case 'tom':
            return 'Tom Tinker'
        case 'dick':
            return 'Richard Tailor'
        case 'harry':
            return 'Harold Soldier'
        case _:
            return 'ERROR: INVALID RECIPIENT VALUE'

# Read user input.
recipient, result = argv[1], argv[2]

# Embed user input data into text and copy to clipboard.
copy(f'''Hi {assign_recipient(recipient)},

Thank you for you hard work on this.

{assign_result(result)}.

Please see the attached Test Method document, for further details of the tests:

Should you have any questions or concerns, please do not hesitate to contact us.

Many thanks!
''')
```

## Pg 147 - Modifying clipboard text
Copy some text to the clipboard. Transform it. Then replace the clipboard text with the transformed text.
```python
from pyperclip import copy, paste
from sys import argv

input_text = paste()
modified_text = input_text.upper()
output_text = copy(f'{modified_text} [This is modified]')
```

## Pg 154 - Table Printer
Transpose data and set the column widths to the widest data within each column (to optimise spacing).
```python
fruit = ['apple', 'pear', 'coconut', 'fig']
names = ['Tom', 'Dick', 'Harry', 'Hercules',]
animals = ['cat', 'dog', 'horse', 'parrot']

los = [fruit, names, animals]

def get_widths(los):
    widths = []
    for i, k in enumerate(los):
        string_lengths = [len(j) for j in k]
        widths.append(max(string_lengths))
    return widths

def set_widths(entry):
    merged = [j[0].ljust(j[1], ' ') for j in entry]
    merged = ' '.join(merged)
    return merged

transpose = [list(row) for row in zip(*los)]
widths = get_widths(los)
assigned = [list(zip(i,widths)) for i in transpose]
formatted = map(set_widths, assigned)
print('\n'.join(formatted))
```
```
apple   Tom      cat
pear    Dick     dog
coconut Harry    horse
fig     Hercules parrot
```
