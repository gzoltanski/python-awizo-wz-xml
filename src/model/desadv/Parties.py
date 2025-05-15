from src.model.self.desadv.Buyer import Buyer
from src.model.self.desadv.Seller import Seller
from src.model.self.desadv.DeliveryPoint import DeliveryPoint
from .base import DesadvBase

class Parties(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)
        self.parties = self.desadv.root.find(f'.//Parties')
        self.buyer = self.parties.find('./Buyer') or self.parties.find('./BUYER')
        self.seller = self.parties.find('./Seller') or self.parties.find('./SELLER')
        self.delivery_point = self.parties.find('./DeliveryPoint') or self.parties.find('./DELIVERY_POINT')
    buyer: Buyer
    seller: Seller
    delivery_point: DeliveryPoint