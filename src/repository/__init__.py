from db.database import Database
from more_itertools import first

class SqlQuery():
     def __init__(self, db: Database, query: str):
         self.cursor = db.cursor
         self.query = query

     def fetch_all(self) -> object:
         self.cursor.execute(self.query)
         return self.cursor.fetchall()

     def fetch_one(self) -> object:
         self.cursor.execute(self.query)
         return self.cursor.fetchone()
