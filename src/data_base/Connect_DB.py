import sqlite3

class Connect_DB:
    def __init__(self, name_db):
        self.name_db = name_db
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.name_db)
            #print('Connection to Successfully')
            return self.connection
        except sqlite3.Error as e:
            print(f'Error connecting to data base: {e}')

    def close_connection(self):
        if self.connection is not None:
            self.connection.close()
            #print('Connection closed successfully')
        else:
            print('No active connect to close')


