# SQL
_Structured Query Language_ (SQL) (pronounced “ess-cue-el" or “sequel”), is a programming language tailored to relational database management. A _database management system_ (DBMS) stores _structured data_ in _tables_ for later queries. A _relational database management system_ (RDBMS) stores data in tables that have relationships between one another. SQL is built to manage RDBMSs. Tables are organised into rows and columns. Columns are associated with a _label_. Rows are associated with a _record_. Each record is associated with a unique identifier known as the _primary key_. 

## Using SQL
There are many means and applications to access databases and submit SQL commands. Examples include _Microsoft Access_, _Microsoft SQL Server_, _Microsoft Visual Studio_, _The Oracle database_, _The IBM database_, _mySQL_, _Python_ _Microsoft Word_ and _Microsoft Excel_. Since some of these applications are not specifically built to handle SQL queries, an _open database connectivity_ (ODBC) is often required. 

## Submitting Queries
SQL commands are called _queries_. Each SQL query must be followed by a semicolon (```;```) which also acts a delimiter, allowing queries to be chained sequentially. Query keywords are not case sensitive, but the convention is to use block capitals. Label and database names are case sensitive and should not include spaces or special characters. NB: This can differ between Windows and Linux operating systems. 

## Viewing All Databases
To see all existing databases, use ```SHOW DATABASES;```.  

## Creating a Database
To create a database, use ```CREATE DATABASE <name>;```.

```sql
CREATE DATABASE peroidic_table.db
```

If the database already exists and this command is used. An error message will display. To ignore this, use ```CREATE DATABASE IF NOT EXISTS <name>```. 

To delete a database, use the ```DROP DATABASE <name>;``` or  ```DROP DATABASE IF EXISTS <name>;``` command. 

SQL commands can be saved to ```.sql``` files as scripts. 

Single-line comments may be inserted in scripts using ```# <text>```, ```-- <text>```. Multiline comments may be inserted via ```/* <text> */```. 

To access a database, use ```USE <database-name>;```. This query must be made before any commands relating to the database’s contents. 

To view the tables within a database, use ```SHOW TABLES;```. 

To view table metadata (columns, data types, restrictions, etc) use ```EXPLAIN <table-name>;```.  

To create tables within a database, use ```CREATE TABLE <name>( 

Column1 datatype1, 

Column2 datatype1);```  

Or ```CREATE TABLE IF NOT EXISTS <name>( 

Column1 datatype1, 

Column2 datatype1);``` 

To delete a table, use ```DROP TABLE <table-name>``` or ```DROP TABLE IF EXISTS <table-name>```. 

Multiple tables can be deleted by via ```DROP TABLE <table1>, <table2>``` 


# SQLite3
## Connecting to an existing database
The examples here ustilise ```sqlite3```, but most of the queries are ubiquitous across different applications. The most notable difference is that ```sqlite3``` databases are stored locally as ```.db``` files. As such, ```sqlite3``` allows for serverless manipulation of SQL databases. It can be imported as a module within Python. 
```python
import sqlite3
```

In ```sqlite3``` if the ```.db``` file doesn't already exist, it will be automatically created simply by connecting to it. Once connected, the contents of the datbase can be manipulated.

```python
import sqlite3 as sql
connection = sql.connect('elements.db')
```









 






#### Executing SQL queries 
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