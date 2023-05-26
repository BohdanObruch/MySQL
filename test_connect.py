import mysql.connector
from dotenv import dotenv_values

dotenv = dotenv_values()
password = dotenv.get('PASSWORD')

# Establishing a database connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password=f'{password}',
    database='voitixler'
)

# Creating a Cursor Object
cursor = conn.cursor()

# Executing a SQL query
cursor.execute('SELECT * FROM operation')

# Get description of columns
columns = [column[0] for column in cursor.description]

# Header output
print(columns)

# Getting all rows of a query result
rows = cursor.fetchall()

# Output of results
for row in rows:
    print(row)

# Saving changes and closing the connection
conn.commit()
conn.close()

# if necessary, in the form of a table with its boundaries

# import mysql.connector
# from tabulate import tabulate
# from dotenv import dotenv_values
#
# dotenv = dotenv_values()
# password = dotenv.get('PASSWORD')
#
# # Establishing a database connection
#
# conn = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password=f'{password}',
#     database='voitixler'
# )
#
# # Creating a Cursor Object
# cursor = conn.cursor()
#
# # Executing a SQL query
# cursor.execute('SELECT * FROM operation')
#
# # Getting column descriptions
# columns = [column[0] for column in cursor.description]
#
# # Getting all rows of the query result
# rows = cursor.fetchall()
#
# # Formatting results as a table
# table = tabulate(rows, headers=columns, tablefmt='pretty')
#
# # Table output
# print(table)
#
# # Saving changes and closing the connection
# conn.commit()
# conn.close()
