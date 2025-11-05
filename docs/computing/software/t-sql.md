# NOTES ON SQL variations.
All variations of SQL use the ```SELECT```, ```INSERT```, ```UPDATE``` and ```DELETE``` statements. They often vary in their database connection and creation protocols, security and qulaity-of-life features.

# General 
Programming languages may be categorised as _procedural_ or _declarative_. Procedural languages require instructions that the user specifies. Declarative languguages require a description of the deisred output. As such, SQL is a declarative language. 

The _primary key_ is used as the definite label for a table's contents. It's usually a unique identifier column in the table (e.g. "UserID"). A _foreign key_ is a reference to a primary key from the perspective of a separate table.

Set theory is important for SQL as you are often considering whole columns of data of the same type (i.e. a mathematical _set_). NB: the ordering of a set is usually irrelevant unless you specifically order it yourself.

SQL uses heirarchical naming conventions to manage data. For instance Data may be stored in a _server_ that caontanins _databases_ that are divided into _schemas_ that include tables. As such, the unanmbiguous (_fully qualified_) name of a table is ```<Server>.<Database>.<Schema>.<Table>```. 

SQL statements can be further subdivided into:
- Data Manipulation Language (DML): Vieiwing and updating data in tables (```SELECT```, ```UPDATE```, ```INSERT```, ```DELETE```).
- Data Definition Language (DDL): Creating, updating and deleting tables (```CREATE```, ```ALTER```, ```DROP```).
- Data Control Language (DCL): Security (```GRANT```, ```REVOKE```, ```DENY```). 
- Transaction COntrol Language (TCL): 
- Data Modification Language: Modifying data in tables only (```UPDATE```, ```INSERT```, ```DELETE```).
- Data Query Language: Querying only (```SELECT```)
DML statements are routinely used for Create, Read, Update and Delete (CRUD) operations.

NB: The order of operations in an SQL statement is not necessarily the order in which server executes them (e.g. ```FROM``` would be executed before ```SELECT``` because the table to search must first be declatred)

NB: Beware data type clases when using arithmentic operators. For example ```+``` can be used for string contcatenation and numeric addition.

# Transact-SQL
Transact-SQL (T-SQL) is a variation of the SQL programming language tailored specifically to Microsoft products.

## Quering Data

All data in a table.
```sql
SELECT * FROM Schema.Table;
```

Only specific columns
```sql
SELECT Column_1, Column_2 FROM Schema.Table;
```

Executing simple fomatting and arithmetic operations and adding _aliases_ as new column headers.
```sql
SELECT Column_1 AS A, '(' + Column_2 + ')' AS B, Column_3 - Column_4 AS C 
FROM Schema.Table;
```

## Converting Data Types

Using ```CAST``` will convert all values in a column to the specified data type. 
Incompatible conversions (e.g. letter to number) will throw an error.
```sql
SELECT 'Unit' + CAST(Num AS varchar(2)) + ': ' AS Column_1
FROM Schema.Table;
```

Using ```TRY_CAST``` will convert all values in a column to the specified data type.
However, if an incompatible conversion is encountered, the returned value will be ```NULL```. 
This may useful for ignoring or isolating certain data within a column.
```sql
SELECT 'Unit' + TRY_CAST(Num AS varchar(2)) + ': ' AS Column_1
FROM Schema.Table;
```
T-SQL also uses ```CONVERT``` and ```TRY_CONVERT``` which allows for additional formattting alongside conversion.

```PARSE``` and ```TRY_PARSE``` are specifically used to convert string data to numeric or date/time values.

```STR``` is used to convert numeric data types to strings (varchar). 

## NULL Values
```NULL``` values are good for placeholders for missing data.
```ISNULL``` can be used to replace ```NULL``` values in a dataset. 
In this example, the user's middlename is replaced with "Not Given" if ```NULL``` is detected.
```sql
SELECT Forename, ISNULL(MiddleName, 'Not Given'), Surname
FROM Schema.Table;
```

## COALESCE
The ```COALESCE``` statement may be used to select different elements in terms of their priority. 
In this example a customer's membership tier can be extracted from 1 of three possibilities, since the other two will be ```NULL```.
```sql
SELECT Custormer, COALESCE('Platinum', 'Gold', 'Silver') AS Membership_Tier
FROM Schema.Table;
```
NB: ```COALESCE``` prioritises the first acceptable element it enconters. Therefore, order each of these elements carefully to ensure that the correct elements are prioritised.

## NULLIF
```NULLIF``` returns ```NULL``` with additional logic. 
As such, it can be useful for replacing certain values with ```NULL```.
This example sets an employee bonus to ```NULL``` if their contribution is 0.
```sql
SELECT NULLIF(Contribution, 0) AS Yearly_Bonus
FROM Schema.Table;
```

