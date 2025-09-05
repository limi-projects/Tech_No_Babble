# SQLite
SQLite allows for serverless manipulation of SQL databases. 
It can be imported as a module within Python as ```sqlite3```.

## Database Creation and Connection
Databases stored locally as .db files and may be accesssed using the ```connect()``` method.
```python
from sqlite3 import connect
establish_connection = connect('periodic_table.db')
```
If the .db file doesn't exist, it will be automatically created.

## Executing SQL queries 
The ```cursor()``` method is used to execute SQL queries.
The below code creates a table called structure within the ```periodic_table.db``` file. 
```python
import sqlite3
connection = sqlite3.connect('periodic_table.db')
db_query = connection.cursor()

db_query.execute('''
    CREATE TABLE structure(
        Name varchar(255),
        Protons int,
        Neutrons int,
        Electrons int)
        ''')

connection.commit()
connection.close()
```
The below code adds a row of data to the structure table within the ```periodic_table.db``` file. 
```python
import sqlite3
connection = sqlite3.connect('periodic_table.db')
db_query = connection.cursor()

db_query.execute('''
    INSERT INTO structure (Name, Protons, Neutrons, Electrons)
    VALUES 
    ('Hydrogen', 1, 0, 1),
    ('Helium', 2, 2, 2)
    ''')

connection.commit()
connection.close()
```
The below code extracts all of the data from the structure table within the ```periodic_table.db``` file.
```python
import sqlite3
connection = sqlite3.connect('periodic_table.db')
db_query = connection.cursor()
db_query.execute('SELECT * FROM structure')
rows = db_query.fetchall()

print(rows)

db_query.close()
```
#### [Back](README.md)
