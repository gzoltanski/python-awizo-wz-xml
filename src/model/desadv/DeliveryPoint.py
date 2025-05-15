from src.model.desadv import *

class DeliveryPoint:
    def __init__(self, desadv_file: Path):
        desadv = XmlDocument(desadv_file)
        self.delivery_point = desadv.root.find("./DespatchAdvice-Parties/DeliveryPoint")
        self.iln = self.delivery_point.find("./ILN")

    def set_iln(self, new_iln):
        self.iln.text = new_iln

    def get_iln(self):
        return self.iln.text