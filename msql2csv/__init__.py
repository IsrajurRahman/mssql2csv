import pyodbc
import pandas.io.sql as psql


class SQLExtractor:
    """
        This class defines the basic functions to convert
        the MS SQL database tables to CSV.
    """
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    def connect_to_database(self):
        """
            Connects to datbase
        """
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=' + self.server + '; '
                      'Database='+ self.database + ';'
                      'UID='+ self.username + ';'
                      'PWD='+ self.password + ';'
                      'Trusted_Connection=yes;')
            print('DATABASE CONNECTED')
            return conn
        except Exception as exc:
            print(f'DATABASE ERROR: {exc}')

    def get_table_list(self, conn):
        """
            Fetches all table names from given database
        """
        try:
            sql = "SELECT TABLE_NAME FROM [" + self.database + "].INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"
            cursor = conn.cursor()
            cursor.execute(sql)
            for (table_name,) in cursor:
                print(table_name)
        except Exception as exc:
            print(f'DATABASE ERROR: {exc}')

    def convert_to_csv(self, conn, table_name):
        """
            Converts given database table to csv.
        """
        try:
            sql = "SELECT * FROM " + self.database + ".dbo." + table_name
            df = psql.read_sql(sql, conn)
            df.to_csv(table_name + ".csv", index=False)
            print(f'table '+ table_name + ' saved as ' + table_name + '.csv')
        except Exception as exc:
            print(f'DATABASE ERROR: {exc}')
