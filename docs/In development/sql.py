# Import modules.
import sqlite3 as sql

# Establish connection to database.
connection = sql.connect('permutator.db')
query = connection.cursor()

# Create a table.
query.execute(
    '''
    CREATE TABLE IF NOT EXISTS options(
    Name varchar(255),
    State_1 varchar(255),
    State_2 varchar(255),
    State_3 varchar(255)
    )'''
)

# Create a table.
query.execute(
    '''
    CREATE TABLE IF NOT EXISTS conditions(
    Result varchar(255),
    Requirement_1 varchar(255)
    )'''
)

# Create a table.
query.execute(
    '''
    CREATE TABLE IF NOT EXISTS filters(
    Requirement_1 varchar(255),
    Requirement_2 varchar(255)
    )'''
)

# Add a row.
query.execute(
    '''INSERT INTO options VALUES(
    "1", "a", "b", "c"
    )'''
)

# View table contents.
query.execute('''SELECT * FROM options''')
rows = query.fetchall()
[print(row) for row in rows]

# Delete table.
query.execute('''DROP TABLE IF EXISTS options''')

# Close connections to database.
connection.commit()
connection.close()