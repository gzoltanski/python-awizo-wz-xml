from db.database import *
from model.sscc import *
from repository.sql_queries import *
from more_itertools import first

from src.model.edi_xml_header import EdiXmlHeader

# db = Database(server=ECOD_SERVER, database=ECOD_TEST_DATABASE, uid=ECOD_UID, pwd=ECOD_PWD)
db = Database()
cursor = db.connection.cursor()

# sscc_sql = query_nve_daten(WAWI_DATABASE, cursor, '359001962150910050')[0]
# sscc_sql = next(iter(query_nve_daten(WAWI_DATABASE, cursor, '359001962150910050')))
sscc_sql = first(query_nve_daten(WAWI_DATABASE, cursor, '359001962150910050'))

sscc = SSCC(*sscc_sql)
print()
print(sscc)


edi_xml_sql = first(query_edi_xml_kopf(WAWI_DATABASE, cursor, '4570262609', '5909000496521'))

edi_xml = EdiXmlHeader(*edi_xml_sql)

print(edi_xml)



