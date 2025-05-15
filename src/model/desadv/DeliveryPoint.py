from .import *

class DeliveryPoint(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)
        self.node = self.desadv.root.find(".//DeliveryPoint")
        self.iln = self.node.find("./ILN")

    def get_iln(self) -> str:
        return self.iln.text

    def set_iln(self, new_iln) -> None:
        self.iln.text = new_iln