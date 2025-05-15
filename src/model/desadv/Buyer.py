from src.model.desadv import *

class Buyer:
    def __init__(self, desadv_file: Path):
        desadv = XmlDocument(desadv_file)

        self.buyer = desadv.root.find("./DespatchAdvice-Parties/Buyer")
        self.iln = self.buyer.find("./ILN")

    def set_iln(self, new_iln):
        self.iln.text = new_iln

    def get_iln(self):
        return self.iln.text
