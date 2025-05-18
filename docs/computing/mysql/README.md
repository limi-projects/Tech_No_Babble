# MySQL

MySQL is a relational database management system (RDBMS).
Its purpose is to obtain data from a database.

SQL queries to access and manipulate the database.
Database data is organised into tables.
Relational databases define relationships between tables via shared data columns. 

## SQL 
SQL is a programming language that manipulates relational databases.
SQL keywords are not case sensitive.



### SQL commands
- SELECT: Get data from the database.
- UPDATE: Update data in a database.
- DELETE: Delete data in a database.
- INSERT INTO: Add data to a database.
- CREATE DATABASE: Create a database.
- ALTER DATABASE: Change a database.
- CREATE TABLE: Create a table.
- ALTER TABLE: Change a table.
- DROP TABLE: Delete a table.
- CREATE INDEX: Create a search key.
- DROP INDEX: Delete a search key.




#### Creating new databases
To create a new database use:
```sql
CREATE DATABASE ChemicalElement;
```
```
Query OK, 1 row affected (0.02 sec)
```

#### Viewing exisitng databases
To view existing databases use:
```sql
SHOW DATABSASES;
```
```
+--------------------+
| Database           |
+--------------------+
| ChemicalElement    |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
```

#### Woriking within a database
To select a particular datbase to work within use:
```sql
USE ChemicalElement;
```
```
Database changed
```

#### Creating tables within a database
```sql
CREATE TABLE AtomicStructure (Protons INT, Neutrons INT, Electrons INT);
```
```
Query OK, 0 rows affected (0.07 sec)
```

#### Adding rows to a table
```sql
INSERT INTO AtomicStructure (Protons, Neutrons, Electrons) VALUES (1, 0, 1);
```
```
Query OK, 1 row affected (0.03 sec)
```

#### Adding columns to a table
```sql
ALTER TABLE AtomicStructure ADD Name VARCHAR(255);
```
```
Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

#### Modifying values in a table
```sql
UPDATE AtomicStructure SET Name = 'Hydrogen' WHERE Protons = 1;
```
```
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```

#### Viewing data in a table
The ```SELECT``` statement extracts data from a database and stores it in a _result set_.
```sql
SELECT * FROM AtomicStructure;
```
```
+---------+----------+-----------+----------+
| Protons | Neutrons | Electrons | Name     |
+---------+----------+-----------+----------+
|       1 |        0 |         1 | Hydrogen |
+---------+----------+-----------+----------+
1 row in set (0.00 sec)
```

Data can be filtered using the ```WHERE``` command:
```sql
SELECT * FROM AtomicStructure WHERE Name = 'Hydrogen';
```
```
+---------+----------+-----------+----------+
| Protons | Neutrons | Electrons | Name     |
+---------+----------+-----------+----------+
|       1 |        0 |         1 | Hydrogen |
+---------+----------+-----------+----------+
1 row in set (0.00 sec)
```

##### Where Clause Operators
- A = B: A is equal to B.
- A > B: A is more than B.
- A < B: A is less than B.
- A >= B: A is more than or equal to B.
- A <= B: A is less than or equal to B.
- A <> B or A != B: A is not equal to B.
- A BETWEEN B AND C: A is within a range of values between B and C.
- A LIKE B: Search for B within A.
- A IN (B, C): A is either B or C.

It can also be used to view the currently selected database.
```
SELECT DATABASE();
```
```
+-----------------+
| DATABASE()      |
+-----------------+
| ChemicalElement |
+-----------------+
1 row in set (0.00 sec)
```

### AND

### OR

### NOT
