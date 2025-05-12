from db.database import Database
from more_itertools import first

class SqlQuery():
     def __init__(self, db: Database, query: str):
         self.cursor = db.cursor
         self.query = query

     def execute(self) -> object:
         self.cursor.execute(self.query)
         return self.cursor.fetchall()
