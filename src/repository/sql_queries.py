

def query_edi_xml_kopf(db, cursor, nr_ref, dln):
    """pobranie danych z Wawi z EDI XML KOPF"""
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
      FROM [{db}].[dbo].[DROBIMEX$EDI XML Kopf]
      WHERE [Belegnummer] = '{nr_ref}' and [ILN-Lieferanschrift] = '{dln}' --and [Lieferungsnr_] <> ''
    """
    return run_sql_query(cursor, SQL_EDI_XML_KOPF)
# -----------------------------------------------------------------------------------------------------

def query_sales_header(db, cursor, nr_ref, nr_nab):
    """dane z WAWI z nagłówka zamówienia sprzedaży"""
    SQL_SALES_HEADER =f"""
    SELECT
           [No_] as NrZam
          ,[Your Reference] as NrRef
          ,[Sell-to Customer No_] as NrNab
          ,[Bill-to Customer No_] as NrPlat
          ,FORMAT([Order Date],'yyyy-MM-dd') as DataZam
          ,FORMAT([Shipment Date],'yyyy-MM-dd') as DataDost
          ,[Belegstatus] as StatusDok
          ,[Abrechnungsmodus LS] as TWZ
      FROM [{db}].[dbo].[DROBIMEX$Sales Header]
      where [Your Reference] = '{nr_ref}'
            and [Sell-to Customer No_] = '{nr_nab}'
            /* and [Shipment Date] >= SYSDATETIME() */
    """
    return run_sql_query(cursor, SQL_SALES_HEADER)
# -----------------------------------------------------------------------------------------------------

def query_sales_line(db, cursor, nr_zam):
    """dane z WAWI z wiersza zamówienia sprzedaży"""
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
    FROM [{db}].[dbo].[DROBIMEX$Sales Line] as SL JOIN [{db}].[dbo].[DROBIMEX$Item] as Z 
    ON SL.[No_] = Z.[No_]
    WHERE SL.[Document No_] = '{nr_zam}'
    """
    return run_sql_query(cursor, SQL_SALES_LINE)
# -----------------------------------------------------------------------------------------------------

def query_sscc_zuord(db, cursor, nr_zam, nr_wiersza):
    """dane z Wawi z SSCC Zuordnung"""
    SQL_SSCC_ZUORD = f"""
    SELECT 
           [Belegnr_] as NrZam
          ,[Belegzeilennr_] as NrWiersza
          ,[NVE] as SSCC
          ,FORMAT([Menge], 'N0','pl-pl') as Ilosc
          ,FORMAT([Menge (Gewichtseinheit)], 'N3','pl-pl') as IloscKG    
      FROM [{db}].[dbo].[DROBIMEX$NVE Zuordnung]
      WHERE [Belegnr_] = '{nr_zam}' and [Belegzeilennr_] = {nr_wiersza}
    """
    return run_sql_query(cursor, SQL_SSCC_ZUORD)
# -----------------------------------------------------------------------------------------------------

def query_nve_daten(db, cursor, sscc):
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
      FROM [{db}].[dbo].[DROBIMEX$NVE Daten] as SSCC
      WHERE [Nr_] = '{sscc}'
    """
    return run_sql_query(cursor, SQL_NVE_DATEN)
# -----------------------------------------------------------------------------------------------------

def query_customer_item(db, cursor, customer_name, buyer_item_code):
    SQL_CUSTOMER_ITEM = f"""
    SELECT 
        pc.[name]
       ,ci.[item_no]
       ,ci.[buyer_item_code]
       ,ci.[drobimex_increment]
       ,ci.[customer_increment]
       ,ci.[customer_uom]
    FROM [ecoddb_tst].[dbo].[customer_item] as ci JOIN [ecoddb_tst].[dbo].[parent_customer] as pc 
    ON ci.[parent_customer_id] = pc.[id] 
    WHERE pc.[name] = {customer_name} and ci.[buyer_item_code] = {buyer_item_code}
"""
    return run_sql_query(cursor, SQL_CUSTOMER_ITEM)
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------

def run_sql_query(cursor, query):
    """Funkcja wykonuje komendę SQL i jako wynik zwraca listę rekordów"""
    cursor.execute(query)
    return cursor.fetchall()
# ---------------------------------------