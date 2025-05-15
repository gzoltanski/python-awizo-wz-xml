from src.model.desadv import *
from .base import DesadvBase

class Seller(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)
        self.seller = self.desadv.root.find(f'.//Seller')
        self.iln = self.seller.find('./Iln') or self.seller.find('./ILN')
        self.code_by_buyer = self.seller.find('./CodeByBuyer') or self.seller.find('./CODE_BY_BUYER')
    iln: str
    code_by_buyer: str