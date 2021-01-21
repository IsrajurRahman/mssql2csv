"""
If you want to save MS SQL Database tables to CSV.
msql2csv is a light-weight, easy to use command 
line tool to convert sql to csv. 
Gives a list of database tables, you can convert 
table data to csv format by entering table name. 
"""

__author__ = "Israjur Rahman (israjurr@gmail.com)"
__version__ = "1.0.0"
__copyright__ = "Copyright (c) 2020 Israjur Rahman"
__license__ = "MIT"

from msql2csv import SQLExtractor

print('-' * 80)
print('CONVERT MS SQL DATABASE TABLES TO CSV')
print('-' * 80)

server =  str(input("Enter Server: ")) # 'ISRAJ-IDARE\SQLEXPRESS'
database = str(input("Enter Database Name: ")) # 'TEST_HITACHI'
username = str(input("Enter Username: "))
password = str(input("Enter Password: "))

sql = SQLExtractor(server, database, username, password)
conn = sql.connect_to_database()
print(' ' * 40)
print('Getting '+ database + ' tables . . .')
print('-' * 40)
print('Tables of database ' + database)
print('-' * 40)

list_a = sql.get_table_list(conn)
print(list_a)
print('-' * 40)
print(' ' * 40)

running = True

while running:
    table_name = str(input("Enter Table Name or EXIT: "))

    if table_name.lower() != 'exit':
        sql.convert_to_csv(conn, table_name)
    else:
        conn.close()
        running = False