from src.model import sscc
from src.model.sscc import SSCC
from src.repository import *


def query_sscc(db: Database, sscc: str) -> SSCC:

    SQL_NVE_DATEN = f"""
        SELECT
           [Nr_] as SSCC
          ,[Artikelnr_] as NrZapasu
          ,[Chargennr_] as NrPartii
          ,FORMAT([MHD],'yyyy-MM-dd') as TPS
          ,FORMAT([Menge],'N0') as Ilosc
          ,FORMAT([Nettogewicht],'N3') as IloscKGNetto
          ,FORMAT([Restmenge],'N0') as IloscPoz
          ,FORMAT([Restmenge (Gewichtseinheit)],'N3') as IloscKG_Poz
          FROM [{db.database}].[dbo].[DROBIMEX$NVE Daten] as SSCC
          WHERE [Nr_] = '{sscc}'
        """

    sscc_sql = SqlQuery(db, SQL_NVE_DATEN).fetch_one()

    return SSCC(*sscc_sql)