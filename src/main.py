from db import *
from src import *
from db.database import *
from model.sscc import *
from src.repository import *
from src.repository.assigned_sscc_repository import query_assigned_sscc
from src.repository.customer_item_repository import *
from src.repository.sscc_repository import *
from more_itertools import first

from src.model.customer_item import CustomerItem
from src.model.edi_xml_header import EdiXmlHeader
from src.model.sales_header import SalesHeader
from src.model.sales_line import SalesLine
from src.model.sscc import SSCC

if __name__ == '__main__':

    wawi_db = Database()
    xwawi_db = Database(server=XWAWI_SERVER, database=XWAWI_DATABASE,uid=XWAWI_UID, pwd=XWAWI_PWD)
    ecod_tst_db = Database(server=ECOD_SERVER, database=ECOD_TEST_DATABASE, uid=ECOD_UID, pwd=ECOD_PWD)

    # print(query_sscc(wawi_db, '359001962151251435'))


    # sscc_list = query_assigned_sscc(xwawi_db, 'ZA24-086634-064000', 10000)
    # for sscc in sscc_list:
    #     print(sscc)

    customer_item_list = query_customer_item(ecod_tst_db, 'name', 'buyer_item_code')
    for item in customer_item_list:
        print(item)

    # customer_item_sql = query_customer_item(ecod_tst_db, ecod.cursor,'name','buyer_item_code')
    # customer_item_list = []
    # for ci in customer_item_sql:
    #     customer_item_list.append(CustomerItem(*ci))
    #
    # for ci in customer_item_list:
    #     print(ci)



    # customer_item_list = []
    # for ci in customer_item_sql:
    #     customer_item_list.append(*ci)
    # print(customer_item_list)

    # sscc_sql = query_nve_daten(WAWI_DATABASE, '359001962150910050')[0]
    # sscc_sql = next(iter(query_nve_daten(WAWI_DATABASE, '359001962150910050')))
    # sscc_sql = first(query_nve_daten(WAWI_DATABASE, '359001962150910050'))
    # sscc = SSCC(*sscc_sql)
    # print(sscc)
    #
    # edi_xml_sql = first(query_edi_xml_kopf(WAWI_DATABASE, cursor, '4570262609', '5909000496521'))
    # edi_xml = EdiXmlHeader(*edi_xml_sql)
    # print(edi_xml)

    # ref = '023314012502'
    # nabywca = '08612'
    #
    # sales_header_sql = first(query_sales_header(xwawi.database, xwawi_cursor, ref, nabywca))
    # sales_header = SalesHeader(*sales_header_sql)
    # print(sales_header)
    #
    # nr_zam = sales_header.no
    #
    # sales_line_sql = first(query_sales_line(xwawi.database, xwawi_cursor, nr_zam))
    # sales_line = SalesLine(*sales_line_sql)
    # print(sales_line)
    #
    # for i in range(10000, 30000, 10000):
    #     assigned_ssc_sql = first(query_sscc_zuord(xwawi.database, cursor, nr_zam, i))
    #     assigned_ssc = AssignedSSCC(*assigned_ssc_sql)
    #     print(assigned_ssc)

    # print(awz_xml_folder)
