from db.database import Database
from src.model.wawi.package_loading import PackageLoading
from src.repository import SqlQuery


def query_package_loading(db: Database, order_no: str, item_no: str) -> [PackageLoading]:
    SQL_KOLLI_VERLADUNG = f"""
        SELECT 
             [Auftragsnr_]	   
            ,[Artikelnr_]
            ,[NVE]
            ,[Chargennr_]
            ,[Chargen ID]
            ,FORMAT([MHD],'yyyy-MM-dd') as TPS   
            ,COUNT([Kartonnr_]) as IloscKolli
            ,FORMAT(SUM([Gewicht]),'N3') as Weight   
        FROM [{db.database}].[dbo].[DROBIMEX$Kolli Verladung]
        WHERE [Artikelnr_] = '{item_no}' AND [Auftragsnr_] = '{order_no}' 
        GROUP BY [Auftragsnr_], [Artikelnr_], [NVE], [Chargennr_], [Chargen ID], [MHD]    
"""

    package_loading_sql_list = SqlQuery(db, SQL_KOLLI_VERLADUNG).fetch_all()
    package_loading_list = []
    for package_loading in package_loading_sql_list:
        package_loading_list.append(PackageLoading(*package_loading))

    return package_loading_list