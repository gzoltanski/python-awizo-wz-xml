# wersja z dn. 2024-07-05

# Aplikacja tworzy awizo WZ w formacie EDI XML wym. przez LIDL, na podstawie awiza WZ wyeksportowanego z EDI XML / WAWI
# oraz danych pobranych z bazy SQL WAWI


# import xml.etree.ElementTree as ET
import pyodbc as sql
import os
import shutil
import time

from desadv_xml import *
from ecod_xml import get_xml_file_list, Table, setup_folder, delete_old_files

# Zaincjowanie zmiennych przechowujących nazwy folderów:
awz_xml_folder = 'C:\\awz_xml_py'
arch_awz_folder = 'c:\\awz_xml_py\\arch'
new_awz_subfolder = 'awz_nowe'
new_awz_folder = os.path.join(awz_xml_folder, new_awz_subfolder)

# --------------------------------------------------------------------

# PROD - dane do zbudowania ConnectionString do połaczenia z bazą SQL WAWI:
DRIVER = 'ODBC Driver 17 for SQL Server'
SERVER = '30-sql024-v\\wawi'
DATABASE = 'wawi-dx'
UID = 'wawi_dataR_user'
PWD = '.M!Y93A*xQ8i'

# TEST - dane do zbudowania ConnectionString do połaczenia z bazą SQL XWAWI:
XDRIVER = 'ODBC Driver 17 for SQL Server'
XSERVER = '30-sql100-v'
XDATABASE = 'xwawi-dx'
XUID = 'sql_xwawi_reader'
XPWD = 'Bp-LcwP9WAo7sTVv'


# połączenie do bazy produkcyjnej WAWI --> zakomentować ponizsze wiersze
# połączenie do bazy testowej XWAWI --> odkomentować ponizsze wiersze

# DRIVER = XDRIVER
# SERVER = XSERVER
# DATABASE = XDATABASE
# UID = XUID
# PWD = XPWD

print(f"\nPracujesz na bazie: {DATABASE}\n")
# Zainicjowanie sesji połaczenia z bazą danych SQL:
# con = sql.connect(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={UID};PWD={PWD}")
con = sql.connect(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={UID};PWD={PWD}")
cursor = con.cursor()

# Do list zainicjowanych poniżej zapiszemy dane pobrane z Wawi (SSCC przyp. do zam., kody EAN, ilości, partie, TPS...)
# Dane w listach muszą być zapisane w kolejności odpowiadającej numerom wierszy zamówienia
# Dane z list zostaną pobrane i zapisane do struktury XML dok. awizo WZ

# lista zaw. n-ry wierszy awiza WZ --> <LineNumber>
awzln_list = []

# lista zaw. n-ry wierszy zamówienia --> <OrderLineNumber>
oln_list = []

# lista zaw. n-ry SSCC palet przyp. do zamówienia --> <SerialNumber>
sscc_list = []

# lista zaw. n-ry kody EAN zapasów --> <EAN>
karton_ean_list = []

# lista zaw. n-ry zapasów nabywcy --> <BuyerItemCode>
bic_list = []

# lista zaw. ilości zapasów wysłanych  --> <QuantityDespatched>
qd_list = []

# lista zaw. JM zapasów --> <UnitOfMeasure>
uom_list = []

# lista zapasów z zamówienia
item_list = []

# lista zaw. nazwy zapasów --> <ItemDescription>
i_desc_list = []

# lista zaw. TPS zapasów --> <BestBeforeDate>
bbd_list = []

# lista zaw. n-ry partii zapasów --> <ID-Begin>
id_begin_list = []

# ---------------------------------------
# pobranie danych z pliku lidl_increments.csv
inc_file = os.path.join(setup_folder,'lidl_increments.csv')
tab_inc = Table(inc_file,';')

def run_sql_query(query):
    """Funkcja wykonuje komendę SQL i jako wynik zwraca listę rekordów"""
    cursor.execute(query)
    return cursor.fetchall()
# ---------------------------------------

def query_edi_xml_kopf(nr_ref, dln):
    """pobranie danych z Wawi z EDI XML KOPF"""
    SQL_EDI_XML_KOPF = f"""
    SELECT
         [Lfd_ Nr_] as NrZapisuNagl
        ,[Belegfunktion] as TypDokEDI
        ,[Belegnummer] as NrRef
        ,FORMAT(SYSDATETIME(),'yyyy-MM-dd') as DataSystem
        ,FORMAT([Lieferdatum],'yyyy-MM-dd') as DataDostawy
        ,[ILN-Käufer] as GLN_Nab
        ,[ILN-Lieferanschrift] as DLN
        ,[übernommen] as StanEDI
        ,[Lieferungsnr_] as NrWZ
        ,[Fremderfassercode] as KodNabywcy
        ,[Verk_ an Deb_-Nr_] as NrNabywcy
      FROM [{DATABASE}].[dbo].[DROBIMEX$EDI XML Kopf]
      WHERE [Belegnummer] = '{nr_ref}' and [ILN-Lieferanschrift] = '{dln}' and [Lieferungsnr_] <> ''
    """
    return run_sql_query(SQL_EDI_XML_KOPF)
# -----------------------------------------------------------------------------------------------------

def query_sales_header(nr_ref, nr_nab):
    """dane z WAWI z nagłówka zamówienia sprzedaży"""
    SQL_SALES_HEADER =f"""
    SELECT
           [Your Reference] as NrRef
          ,[No_] as NrZam
          ,[Sell-to Customer No_] as NrNab
          ,[Bill-to Customer No_] as NrPlat
          ,FORMAT([Order Date],'yyyy-MM-dd') as DataZam
          ,FORMAT([Shipment Date],'yyyy-MM-dd') as DataDost
          ,[Belegstatus] as StatusDok
          ,[Abrechnungsmodus LS] as TWZ
      FROM [{DATABASE}].[dbo].[DROBIMEX$Sales Header]
      where [Your Reference] = '{nr_ref}'
            and [Sell-to Customer No_] = '{nr_nab}'
            /* and [Shipment Date] >= SYSDATETIME() */
    """
    return run_sql_query(SQL_SALES_HEADER)
# -----------------------------------------------------------------------------------------------------

def query_sales_line(nr_zam):
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
    FROM [{DATABASE}].[dbo].[DROBIMEX$Sales Line] as SL JOIN [{DATABASE}].[dbo].[DROBIMEX$Item] as Z 
    ON SL.[No_] = Z.[No_]
    WHERE SL.[Document No_] = '{nr_zam}'
    """
    return run_sql_query(SQL_SALES_LINE)
# -----------------------------------------------------------------------------------------------------

def query_sscc_zuord(nr_zam, nr_wiersza):
    """dane z Wawi z SSCC Zuordnung"""
    SQL_SSCC_ZUORD = f"""
    SELECT 
           [Belegnr_] as NrZam
          ,[Belegzeilennr_] as NrWiersza
          ,[NVE] as SSCC
          ,FORMAT([Menge], 'N0','pl-pl') as Ilosc
          ,FORMAT([Menge (Gewichtseinheit)], 'N3','pl-pl') as IloscKG    
      FROM [{DATABASE}].[dbo].[DROBIMEX$NVE Zuordnung]
      WHERE [Belegnr_] = '{nr_zam}' and [Belegzeilennr_] = {nr_wiersza}
    """
    return run_sql_query(SQL_SSCC_ZUORD)
# -----------------------------------------------------------------------------------------------------

def query_nve_daten(sscc):
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
      FROM [{DATABASE}].[dbo].[DROBIMEX$NVE Daten] as SSCC
      WHERE [Nr_] = '{sscc}'
    """
    return run_sql_query(SQL_NVE_DATEN)
# -----------------------------------------------------------------------------------------------------

def create_desadv_lidl(wawi_desadv_filename):
    """Funkcja przetwarza plik awiza WZ z WAWI i tworzy plik awiza zgodny z wtm LIDL"""

    # utworzenie obiektu klasy DesadvXML dla awiza WZ XML
    awz = DesadvXML(wawi_desadv_filename)
    # wyswietlenie na ekranie struktury drzewa XML oryginalnego pliku awiza
    # awz.display_xml_tree()

    NrReferencji = awz.get_buyer_order_number()
    print(f"(2) NrReferencji = {NrReferencji}")         # 2 wydr. wiersz

    DLN = awz.get_dln()
    print(f"(3) DLN = {DLN}")       # 3 wydr. wiersz

    nr_zapisu_edi_kopf_list = []
    nab_list = []
    # pobranie danych z nagłówka EDI XML (przez kwerendę SQL):
    edi_kopf = query_edi_xml_kopf(NrReferencji, DLN)
    for ek in edi_kopf:
        nr_zapisu_edi_kopf_list.append(ek.NrZapisuNagl)
        nab_list.append(ek.NrNabywcy)

    try:
        NrZapisuNagl = nr_zapisu_edi_kopf_list[0]
    except IndexError:
        print(f"\n\n!!! BRAK ZAMÓWIENIA EDI W WAWI W EDI XML !!!\n\n")
        exit('Zakończenie działania programu wskutek błędu! ')
    NrNabywcy = nab_list[0]
    print(f"(4) NrZapisuNagl = {NrZapisuNagl}\n(5) NrNabywcy = {NrNabywcy}\n")      # 4 i 5 wydr. wiersz
    # inicjujemy listy do których zapiszemy dane pobrane kw. SQL z zam. sprzed.
    ListaZam = []   # n-r zam sprzedaży
    ListaTWZ = []   # kod trybu wydruku WZ
    ListaRef = []   # n-r zam. wg nabywcy

    # Pobieramy dane z Wawi SQL z nagł. zam. sprzed. ...
    s_headers = query_sales_header(NrReferencji, NrNabywcy)

    # ... i dopisujemy do odpowiednich list
    for sh in s_headers:
        ListaZam.append(sh.NrZam)
        ListaRef.append(sh.NrRef)
        ListaTWZ.append(sh.TWZ)

    NrZam = ListaZam[0]
    NrRefZam = ListaRef[0]
    TWZ = ListaTWZ[0]
    print(f"(6) NrZam = {NrZam}")   # 6 wydr. wiersz
    print(f"(6.1) NrRefZam = {NrRefZam}")   # 6.1 wydr. wiersz
    print(f"(6.2) TWZ = {TWZ}")   # 6.2 wydr. wiersz

    awz_ln = 0  # licznik wierszy awiza WZ
    jm = ''     # zmienna na JM do zapisania do pliku XML awiza WZ

    wiersze_zam = query_sales_line(NrZam)   # pobierz wiersze zamówienia z tab. SQL Sales Line z WAWI
    for w in wiersze_zam:   # z każdego wiersza pobierz dane i zapisz w zmiennych...
        nr_wiersza_zam = w.NrWiersza
        opis_zapasu = w.Nazwa
        nr_zapasu_nab = w.NrZapasuNab
        print(f"Nr zapasu nabywcy: {nr_zapasu_nab}")
        kod_karton_ean = w.KartonEAN
        if w.JM == 'SZT':   # jeśli w wierszu zamówienia mamy JM = 'SZT'
            jm = 'PCE'      # ...to zapisz jako 'PCE' (w pliku XML j.m. sztuka to PCE

        jm_tab_inc = tab_inc.get_uom_by_cust_item(nr_zapasu_nab)    # JM pobrana z tab. inkrementów
        inkrem_tab_inc = tab_inc.get_dx_inc_by_cust_item(nr_zapasu_nab) # inkrement z tab. inkrementów

        przyp_sscc = query_sscc_zuord(NrZam, nr_wiersza_zam)  # z każdego wiersza pobierz przypisania SSCC (kw. SQL)
        for p_sscc in przyp_sscc:      # ...dla każdej palety przypisanej do wiersza zamówienia ...
            awzln_list.append(awz_ln + 1)
            oln_list.append(nr_wiersza_zam // 10000)
            sscc = p_sscc.SSCC
            sscc_list.append(sscc)          # dopisz do listy SSCC (SSCC przyp. do zamówienia)
            dane_sscc = query_nve_daten(sscc)[0]  # pobierz dane z tabeli SSCC z WAWI
            id_begin_list.append(dane_sscc.NrPartii)
            bbd_list.append(dane_sscc.TPS)
            # ustalenie ilości JM (szt, kg, kartonów) dla poszczeg. palet w zależności od JM
            ilosc = 0
            if jm_tab_inc == 'kg':
                ilosc = dane_sscc.IloscKGNetto
                print(f"(kg) ilosc: {ilosc}" )
            elif jm_tab_inc == 'szt':
                ilosc_liczba = int(p_sscc.Ilosc) * float(inkrem_tab_inc)
                # print(f"(szt) ilosc_liczba: {ilosc_liczba}")
                ilosc = str(ilosc_liczba)
                print(f"(szt) ilosc: {ilosc}")
            elif jm_tab_inc == 'kart':
                ilosc = p_sscc.Ilosc
                print(f"(kart) ilosc: {ilosc}")

            qd_list.append(ilosc)    # dopisz do listy qd (ilość kartonów na palecie)

            bic_list.append(nr_zapasu_nab)
            i_desc_list.append(opis_zapasu)
            karton_ean_list.append(kod_karton_ean)
            uom_list.append(jm)
    # --------------------------------------------------------------------------------------

    # tworzymy pustą listę "ps_list" dla obiektów <Packing-Sequence> - w skrócie <P-S>
    # w strukturze XML awiza WZ utworzymy tyle obiektów (gałęzi) <P-S> ile mamy palet przypisanych do zamówienia
    # utworzone obiekty <P-S> zapiszemy w "ps_list"
    ps_list = []

    # w oryginalnym awizo WZ XML, usuwamy ze struktury XML sekcję <Packing-Sequence>
    # sekcje <P-S> zostaną utworzone od nowa, w ilości odpowiadającej liczbie palet przyp. do zamówienia
    awz.clear_da_consigment()

    # w każdej sekcji <P-S> (czyli dla każdego z tworzonych obiektów <P-S>) utworzymy podsekcje, do których zapiszemy
    # wymagane dane do AWZ (pobrane wcześniej z WAWI i zapisane osobnych listach)
    # w poniższej pętli "for" tworzymy obiekty (sekcje) <P-S> oraz odpowiednie podsekcje dla każdego z nich
    # w nowo utworzonych elementach drzewa XML od razu zapisujemy wymagane dane dla awiza WZ, pobrane wcześniej z WAWI
    # i zapisane w odpowiednich listach;
    # w ten sposób uzupełnimy strukturę XML awiza WZ o wymagane dane;
    i = 0
    for sscc in sscc_list:              # ilość iteracji = ilość sscc (czyli palet) przyp. do zamówienia
        i += 1
        ps_list.append(ET.SubElement(awz.DespatchAdvice_Consignment, "Packing-Sequence"))
        ET.indent(awz.root, space='  ', level=1)

        pr = ET.SubElement(ps_list[i-1], "Packing-Reference")
        ET.indent(awz.root, space='  ', level=2)

        pid = ET.SubElement(pr, "PackageId")
        pn = ET.SubElement(pr, "PackageNumber")
        pt = ET.SubElement(pr, "PackageType")
        sn = ET.SubElement(pr, "SerialNumber")
        ET.indent(awz.root, space='  ', level=3)

        pid.text = str(i)
        pn.text = str(len(sscc_list))
        pt.text = str('201')
        sn.text = str(sscc)

        line = ET.SubElement(ps_list[i-1], "Line")
        ET.indent(awz.root, space='  ', level=2)

        l_item = ET.SubElement(line, "Line-Item")
        ET.indent(awz.root, space='  ', level=3)

        ln = ET.SubElement(l_item, "LineNumber")
        oln = ET.SubElement(l_item, "OrderLineNumber")
        ean = ET.SubElement(l_item, "EAN")
        bic = ET.SubElement(l_item, "BuyerItemCode")
        qd = ET.SubElement(l_item, "QuantityDespatched")
        uom = ET.SubElement(l_item, "UnitOfMeasure")
        i_desc = ET.SubElement(l_item, "ItemDescription")
        bbd = ET.SubElement(l_item, "BestBeforeDate")
        ET.indent(awz.root, space='  ', level=4)

        ln.text = str(i)
        oln.text = str(oln_list[i-1])
        ean.text = str(karton_ean_list[i-1])
        bic.text = str(bic_list[i-1])
        qd.text = str(qd_list[i-1])
        uom.text = str(uom_list[i-1])
        i_desc.text = str(i_desc_list[i-1])
        bbd.text = str(bbd_list[i-1])

        p_ident = ET.SubElement(line, "Package-Identification")
        ET.indent(awz.root, space='  ', level=3)

        g_ident = ET.SubElement(p_ident, "Goods-Identity")
        ET.indent(awz.root, space='  ', level=4)

        typ = ET.SubElement(g_ident, "Type")
        typ.text = 'BX'
        rng = ET.SubElement(g_ident, "Range")
        ET.indent(awz.root, space='  ', level=5)

        id_begin = ET.SubElement(rng, "ID-Begin")
        ET.indent(awz.root, space='  ', level=6)

        id_begin.text = str(id_begin_list[i-1])

    # wyświetlamy na ekranie fragment struktury drzewa XML - od sekcji <DespatchAdvice-Consignment>
    # awz.display_xml_tree_da()
    # zapisujemy nową strukturę XML do nowego pliku awiza WZ XML, do folderu "awz_do_wyslania"
    # nowy plik XML bedzie mozna przesłac na ECOD

    print(f"\nilość palet: {sscc_list.__len__()}")

    awz.save_desadv_xml_file()

    # Zapisanie w archiwum nie przetworzonego pliku awizo WZ XML
    # arch_filename = os.path.join(arch_folder, awz_filename)

    awz.move_to_arch_desadv_xml_file()

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

# tu się zaczyna program :)

delete_old_files(arch_awz_folder)

print(f"{new_awz_folder}")

# Przeszukujemy folder zaw. awiza WZ i zapisujemy nazwy plików awiz WZ XML do listy
awz_filename_list = get_xml_file_list(new_awz_folder)

print(f"\nlista awiz WZ:")

for awz in awz_filename_list:
    print(f"{awz}")

print()
for awz in awz_filename_list:
    print('\n=======================================================================\n')

    create_desadv_lidl(awz)

    awzln_list = []
    oln_list = []
    sscc_list = []
    karton_ean_list = []
    bic_list = []
    qd_list = []
    uom_list = []
    item_list = []
    i_desc_list = []
    bbd_list = []
    id_begin_list = []