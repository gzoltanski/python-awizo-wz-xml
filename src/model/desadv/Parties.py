from dataclasses import dataclass
from src.model.desadv.Buyer import Buyer
from src.model.desadv.Seller import Seller
from src.model.desadv.DeliveryPoint import DeliveryPoint

@dataclass
class Parties:
    buyer: Buyer
    seller: Seller
    delivery_point: DeliveryPoint