from db.database import Database
from src.model.wawi.sales_line import SalesLine
from src.repository import SqlQuery


def query_sales_line(db: Database, order_no: str) -> [SalesLine]:

    SQL_SALES_LINE = f"""
        SELECT
           SL.[Document No_] as NrDok
    	  ,SL.[Line No_] as NrWiersza
          ,SL.[No_] as NrZapasu
    	  ,SL.[Kunden-Artikelnr_] as NrZapasuNab
          ,SL.[Description] as Nazwa
          ,SL.[Kunden-EAN] as EAN
    	  ,Z.[EAN (enth_ Einheit)] as KartonEAN
          ,FORMAT(SL.[Quantity],'N3','pl-pl') as Ilosc
          ,FORMAT(SL.[Qty_ to Ship],'N3','pl-pl') as IloscDoWysl
          ,SL.[Unit of Measure Code] as JM
          ,FORMAT(SL.[Quantity (Base)],'N3','pl-pl') as IloscBaz
          ,FORMAT(SL.[Qty_ to Ship (Base)],'N3','pl-pl') as IloscDoWyslBaz
    	  ,SL.[Haltbarkeitstage] as DniTPS
    	  ,FORMAT(SL.[Shipment Date] + SL.[Haltbarkeitstage],'yyyy-MM-dd') as DataTPS
          ,SL.[Lieferfreigabe] as Zwoln
          ,FORMAT(SL.[Bestellgewicht (Soll)],'N3','pl-pl') as IloscKG_Zam
        FROM [{db.database}].[dbo].[DROBIMEX$Sales Line] as SL JOIN [{db.database}].[dbo].[DROBIMEX$Item] as Z 
        ON SL.[No_] = Z.[No_]
        WHERE SL.[Document No_] = '{order_no}'
        """

    sales_line_sql_list = SqlQuery(db, SQL_SALES_LINE).fetch_all()
    sales_line_list = []
    for sales_line in sales_line_sql_list:
        sales_line_list.append(SalesLine(*sales_line))

    return sales_line_list