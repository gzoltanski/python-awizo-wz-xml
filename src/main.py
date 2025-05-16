from db.database import *
from src import *
from src.model.desadv.Consignment import Consignment
from src.model.desadv.DeliveryPoint import DeliveryPoint
from src.model.desadv.Buyer import Buyer
from src.model.desadv.DespatchAdvice import DespatchAdvice
from src.model.desadv.Header import Header
from src.model.desadv.PackingReference import PackingReference
from src.model.desadv.PackingSequence import PackingSequence
from src.model.desadv.Parties import Parties
from src.model.desadv.Seller import Seller
from src.model.desadv.Transport import Transport
from src.repository.wawi.sscc_repository import *

if __name__ == '__main__':

    wawi_db = Database()
    xwawi_db = Database(server=XWAWI_SERVER, database=XWAWI_DATABASE,uid=XWAWI_UID, pwd=XWAWI_PWD)
    ecod_tst_db = Database(server=ECOD_SERVER, database=ECOD_TEST_DATABASE, uid=ECOD_UID, pwd=ECOD_PWD)

    awz_filename = 'WZ24-080686-064000.XML'
    awz_file = new_awz_folder / awz_filename
    print(awz_file)

    despatch_advice = DespatchAdvice(awz_file)
    print(despatch_advice)

    # buyer = Buyer(awz_file)
    # print(buyer)
    #
    # delivery_point = DeliveryPoint(awz_file)
    # print(delivery_point)
    #
    # seller = Seller(awz_file)
    # print(f"Seller - code by buyer: {seller.code_by_buyer.text}")
    # print(seller)
    # seller.code_by_buyer.text = "852145"
    # print(f"Seller - code by buyer: {seller.code_by_buyer.text}")
    # print(seller)
    #
    # header = Header(awz_file)
    # header.despatch_date.text = '2025-05-15'
    # print(header)

    # packing_reference = PackingReference(awz_file)
    # print(packing_reference)

    # parties = Parties(awz_file)
    # print(parties)

    # transport = Transport(awz_file)
    # print(transport)

    # consignment = Consignment(awz_file)
    # print(consignment)

    # packing_sequence = PackingSequence(awz_file)
    # print(packing_sequence)