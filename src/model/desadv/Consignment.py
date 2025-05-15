from . import *
from .PackingSequence import PackingSequence


class Consignment(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)
        self.node = self.desadv.root.find(".//Consignment")
        self.packing_sequence = self.node.find("Packing-Sequence")

    def get_packing_sequence(self) -> PackingSequence:
        return self.packing_sequence