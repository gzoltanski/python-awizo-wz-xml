import pyodbc as db

DRIVER = 'ODBC Driver 17 for SQL Server'

# PROD - dane do zbudowania ConnectionString do połaczenia z bazą SQL WAWI:
WAWI_SERVER = r'30-sql024-v\wawi'
WAWI_DATABASE = r'wawi-dx'
WAWI_UID = r'wawi_dataR_user'
WAWI_PWD = r'.M!Y93A*xQ8i'

# TEST - dane do zbudowania ConnectionString do połaczenia z bazą SQL XWAWI:
XWAWI_SERVER = r'30-sql100-v'
XWAWI_DATABASE = r'xwawi-dx'
XWAWI_UID = r'sql_xwawi_reader'
XWAWI_PWD = 'Bp-LcwP9WAo7sTVv'


# # ECOD Test - dane do zbudowania ConnectionString do połaczenia z bazą EcodDB_TST:
ECOD_SERVER = r'sql1-dx\dbeqsys'
ECOD_DATABASE = r'ecoddb'
ECOD_TEST_DATABASE = r'ecoddb_tst'
ECOD_UID = r'sqla_it'
ECOD_PWD = r'EE9fUYFqPjWx3.gL'

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