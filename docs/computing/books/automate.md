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

## Pg 127 - Chessboard (unfinished)
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
