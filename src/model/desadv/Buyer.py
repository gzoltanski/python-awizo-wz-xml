from src.model.desadv import *
from .base import DesadvBase

class Buyer(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)

        self.buyer = self.desadv.root.find("./DespatchAdvice-Parties/Buyer")
        self.iln = self.buyer.find("./ILN")

    def set_iln(self, new_iln):
        self.iln.text = new_iln

    def get_iln(self):
        return self.iln.text