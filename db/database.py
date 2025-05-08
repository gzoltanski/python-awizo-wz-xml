import pyodbc as db
from db import *

class Database:
    def __init__(self,
                 driver = DRIVER,
                 server = WAWI_SERVER,
                 database = WAWI_DATABASE,
                 uid = WAWI_UID,
                 pwd = WAWI_PWD):

        self.driver = driver
        self.server = server
        self.database = database
        self.uid = uid
        self.pwd = pwd

        self.connection = db.connect(
            f'DRIVER={self.driver};'
            f'SERVER={self.server};' 
            f'DATABASE={self.database};'
            f'UID={self.uid};'
            f'PWD={self.pwd}'
        )
        self.cursor = self.connection.cursor()

    def display_database_name(self):
        return f"\nJesteś połączony z bazą danych: {self.database}"