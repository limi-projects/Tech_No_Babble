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
from itertools import product

def make_board(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

pieces = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'R1', 'R2', 'N1', 'N2', 'B1', 'B2', 'Q', 'K',]
whites = ['w'+p for p in pieces]
blacks = ['b'+p for p in pieces]

row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',]
column = ['1', '2', '3', '4', '5', '6', '7', '8',]

places = product(row, column)
places = [''.join(place) for place in places]
board = list(make_rows(places, 8))

print(whites)
for i in whites:
    if 'P' in i:
        print(i)
#starting_config = {f} 


#print(s[0])
#for i in board:
#    print(i)
#a = places[0:8]
#b = places[8:16]
#c = places[16:24]
#print(c)
#blank_board = {place: ' ' for place in places}
#print(blank_board)
#setup_board = 
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
