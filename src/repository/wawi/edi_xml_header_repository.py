from src.model.wawi.edi_xml_header import EdiXmlHeader
from src.repository import *


def query_edi_xml_header(db: Database, ref_no: str, dln: str ) -> EdiXmlHeader:
    SQL_EDI_XML_KOPF = f"""
        SELECT
             [Lfd_ Nr_] as NrZapisuNagl
            ,[Belegfunktion] as TypDokEDI
            ,[Belegnummer] as NrRef
            --,FORMAT(SYSDATETIME(),'yyyy-MM-dd') as DataSystem
            ,FORMAT([Lieferdatum],'yyyy-MM-dd') as DataDostawy
            ,[ILN-Käufer] as GLN_Nab
            ,[ILN-Lieferanschrift] as DLN
            ,[übernommen] as StanEDI
            ,[Lieferungsnr_] as NrWZ
            ,[Fremderfassercode] as KodNabywcy
            ,[Verk_ an Deb_-Nr_] as NrNabywcy
          FROM [{db.database}].[dbo].[DROBIMEX$EDI XML Kopf]
          WHERE [Belegnummer] = '{ref_no}' and [ILN-Lieferanschrift] = '{dln}' -- and [Lieferungsnr_] <> ''
        """

    edi_xml_header_sql = SqlQuery(db, SQL_EDI_XML_KOPF).fetch_one()

    return EdiXmlHeader(*edi_xml_header_sql)
