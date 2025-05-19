from db.database import *
from src import *
# import src.model.desadv
from src.model.desadv import *
from src.model.desadv.Consignment import Consignment
from src.model.desadv.DeliveryPoint import DeliveryPoint
from src.model.desadv.Buyer import Buyer
from src.model.desadv.DespatchAdvice import DespatchAdvice
from src.model.desadv.GoodsIdentity import GoodsIdentity
from src.model.desadv.Header import Header
from src.model.desadv.PackingReference import PackingReference
from src.model.desadv.PackingSequence import PackingSequence
from src.model.desadv.Line import Line
from src.model.desadv.LineItem import LineItem
from src.model.desadv.Parties import Parties
from src.model.desadv.Seller import Seller
from src.model.desadv.Transport import Transport
from src.model.desadv.Range import Range
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

    print("\n======== sprawdzamy elementy potomne =======\n")
    # for child in despatch_advice.desadv.root:
    #     print(child.tag, child.attrib, child.text)


    def extract_elements(element):

        element_dict = {element.tag: element.text}
        children_list = []
        for child in element:
            children_list.append(extract_elements(child))

        element_dict['children'] = children_list
        return element_dict



    root = despatch_advice.desadv.root
    result = extract_elements(root)

    for key, value in result.items():
        print(key, value)




    # extract_elements(root)

    # consignment = Consignment(awz_file)
    # print(consignment)




    # print("\n======== usuwamy elementy gałęzi <Consignment> =======\n")
    # consignment.clear()
    # print(despatch_advice)

    # print("\n======== sprawdzamy elementy gałęzi <Consignment> =======\n")
    # consignment_list = despatch_advice.get_list_of_consigment()
    # for consigment in consignment_list:
    #     print(consigment)

    #
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
    #
    # packing_reference = PackingReference(awz_file)
    # print(packing_reference)
    #
    # parties = Parties(awz_file)
    # print(parties)
    #
    # transport = Transport(awz_file)
    # print(transport)
    #
    # packing_sequence = PackingSequence(awz_file)
    # print(packing_sequence)
    #
    # range = Range(awz_file)
    # print(range)
    #
    # goods_identity = GoodsIdentity(awz_file)
    # print(goods_identity)
    #
    # line = Line(awz_file)
    # print(line)
    #
    # line_item = LineItem(awz_file)
    # print(line_item)

