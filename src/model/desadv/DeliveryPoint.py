from src.model.desadv import *
from .base import DesadvBase

class DeliveryPoint(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)
        self.delivery_point = self.desadv.root.find("./DespatchAdvice-Parties/DeliveryPoint")
        self.iln = self.delivery_point.find("./ILN")

    def set_iln(self, new_iln):
        self.iln.text = new_iln

    def get_iln(self):
        return self.iln.text