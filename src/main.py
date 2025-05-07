from db.database import *
from model.sscc import *
from repository.sql_queries import *
from more_itertools import first

from src.model.edi_xml_header import EdiXmlHeader
from src.model.sales_header import SalesHeader
from src.model.sales_line import SalesLine
from src.model.assigned_sscc import AssignedSSCC

# db = Database(server=ECOD_SERVER, database=ECOD_TEST_DATABASE, uid=ECOD_UID, pwd=ECOD_PWD)
db = Database()
cursor = db.connection.cursor()
print(db.display_database_name())

# sscc_sql = query_nve_daten(WAWI_DATABASE, cursor, '359001962150910050')[0]
# sscc_sql = next(iter(query_nve_daten(WAWI_DATABASE, cursor, '359001962150910050')))
# sscc_sql = first(query_nve_daten(WAWI_DATABASE, cursor, '359001962150910050'))
# sscc = SSCC(*sscc_sql)
# print(sscc)
#
# edi_xml_sql = first(query_edi_xml_kopf(WAWI_DATABASE, cursor, '4570262609', '5909000496521'))
# edi_xml = EdiXmlHeader(*edi_xml_sql)
# print(edi_xml)

ref = '023308052501'
nabywca = '06664'

sales_header_sql = first(query_sales_header(WAWI_DATABASE, cursor, ref, nabywca))
sales_header = SalesHeader(*sales_header_sql)
print(sales_header)

nr_zam = sales_header.no

sales_line_sql = first(query_sales_line(WAWI_DATABASE, cursor, nr_zam))
sales_line = SalesLine(*sales_line_sql)
print(sales_line)

for i in range(10000, 60000, 10000):
    assigned_ssc_sql = first(query_sscc_zuord(WAWI_DATABASE, cursor, nr_zam, i))
    assigned_ssc = AssignedSSCC(*assigned_ssc_sql)
    print(assigned_ssc)


