from db.database import Database
from src.model.assigned_sscc import AssignedSSCC
from src.repository import SqlQuery


def query_assigned_sscc(db: Database, order_no, line_no) -> [AssignedSSCC]:

    SQL_SSCC_ZUORD = f"""
        SELECT 
               [Belegnr_] as NrZam
              ,[Belegzeilennr_] as NrWiersza
              ,[NVE] as SSCC
              ,FORMAT([Menge], 'N0','pl-pl') as Ilosc
              ,FORMAT([Menge (Gewichtseinheit)], 'N3','pl-pl') as IloscKG    
          FROM [{db.database}].[dbo].[DROBIMEX$NVE Zuordnung]
          WHERE [Belegnr_] = '{order_no}' and [Belegzeilennr_] = {line_no}
        """

    assigned_sscc_sql_list = SqlQuery(db, SQL_SSCC_ZUORD).execute()
    assigned_sscc_list = []
    for sscc in assigned_sscc_sql_list:
        assigned_sscc_list.append(AssignedSSCC(*sscc))

    return assigned_sscc_list