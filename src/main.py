from db.database import *
from src.repository.assigned_sscc_repository import query_assigned_sscc
from src.repository.customer_item_repository import *
from src.repository.edi_xml_header_repository import query_edi_xml_header
from src.repository.package_loading_repository import query_package_loading
from src.repository.sales_header_repository import query_sales_header
from src.repository.sales_line_repository import query_sales_line
from src.repository.sscc_repository import *

if __name__ == '__main__':

    wawi_db = Database(server=WAWI_SERVER, database=WAWI_DATABASE, uid=WAWI_UID, pwd=WAWI_PWD)
    xwawi_db = Database(server=XWAWI_SERVER, database=XWAWI_DATABASE,uid=XWAWI_UID, pwd=XWAWI_PWD)
    ecod_tst_db = Database(server=ECOD_SERVER, database=ECOD_TEST_DATABASE, uid=ECOD_UID, pwd=ECOD_PWD)

    # print(query_sscc(wawi_db, '359001962151251435'))
    #
    #
    # sscc_list = query_assigned_sscc(xwawi_db, 'ZA24-086634-064000', 10000)
    # for sscc in sscc_list:
    #     print(sscc)
    #
    # print(query_sscc(xwawi_db, '359001962120170897'))

    # customer_item_list = query_customer_item(ecod_tst_db,'ALDI', '7720')
    # for item in customer_item_list:
    #     print(item)
    #
    # print(query_edi_xml_header(xwawi_db, '806397', '5900000201177'))
    #
    # print(query_sales_header(xwawi_db, '3500392026', '03271'))
    #
    # sales_line_list = query_sales_line(xwawi_db, 'ZA24-086715-064000')
    # for sales_line in sales_line_list:
    #     print(sales_line)

    package_loading_list = query_package_loading(wawi_db, 'ZA24-136809-064000', '21324')

    for package_loading in package_loading_list:
        print(package_loading)
