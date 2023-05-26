import pyodbc
from dotenv import dotenv_values

dotenv = dotenv_values()
database_name = dotenv.get('DATABASE_SQL_SERVER')
server_name = dotenv.get('SERVER_NAME')

# Establishing a database connection
server = f'{server_name}'
database = f'{database_name}'
conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=' + server + ';'
                      'Database=' + database + ';'
                      'Trusted_Connection=yes;')

# Creating a Cursor Object
cursor = conn.cursor()

# Executing a SQL query
cursor.execute('SELECT * FROM STUDENTS')

# Getting column descriptions
columns = [column[0] for column in cursor.description]

# Header output
print(columns)

# Output of results
for row in cursor:
    print(row)

# Saving changes and closing the connection
cursor.close()
conn.close()



# if necessary, in the form of a table with its boundaries
#
# import pyodbc
# from tabulate import tabulate
#
# dotenv = dotenv_values()
# database_name = dotenv.get('DATABASE_SQL_SERVER')
# server_name = dotenv.get('SERVER_NAME')
#
# # Establishing a database connection
# server = f'{server_name}'
# database = f'{database_name}'
# conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
#                       'Server=' + server + ';'
#                       'Database=' + database + ';'
#                       'Trusted_Connection=yes;')
#
# # Creating a Cursor Object
# cursor = conn.cursor()
#
# # Executing a SQL query
# cursor.execute('SELECT * FROM STUDENTS')
#
# # Getting column descriptions
# columns = [column[0] for column in cursor.description]
#
# # Getting all rows of the query result
# results = cursor.fetchall()
#
# # Formatting results as a table
# table = tabulate(results, headers=columns, tablefmt='pretty')
# print(table)
#
# # Saving changes and closing the connection
# cursor.close()
# conn.close()
