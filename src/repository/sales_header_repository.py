from db.database import Database
from src.model.sales_header import SalesHeader
from src.repository import *


def query_sales_header(db: Database, ref_no: str, customer_no: str ) -> SalesHeader:
    SQL_SALES_HEADER = f"""
        SELECT
               [No_] as NrZam
              ,[Your Reference] as NrRef
              ,[Sell-to Customer No_] as NrNab
              ,[Bill-to Customer No_] as NrPlat
              ,FORMAT([Order Date],'yyyy-MM-dd') as DataZam
              ,FORMAT([Shipment Date],'yyyy-MM-dd') as DataDost
              ,[Belegstatus] as StatusDok
              ,[Abrechnungsmodus LS] as TWZ
          FROM [{db.database}].[dbo].[DROBIMEX$Sales Header]
          where [Your Reference] = '{ref_no}'
                and [Sell-to Customer No_] = '{customer_no}'
                -- and [Shipment Date] >= SYSDATETIME()
        """

    sales_header_sql = SqlQuery(db, SQL_SALES_HEADER).fetch_one()

    return SalesHeader(*sales_header_sql)