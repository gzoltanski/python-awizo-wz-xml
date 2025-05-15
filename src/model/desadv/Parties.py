from dataclasses import dataclass
from src.model.self.desadv.Buyer import Buyer
from src.model.self.desadv.Seller import Seller
from src.model.self.desadv.DeliveryPoint import DeliveryPoint
from .base import DesadvBase

@dataclass
class Parties(DesadvBase):
    buyer: Buyer
    seller: Seller
    delivery_point: DeliveryPoint