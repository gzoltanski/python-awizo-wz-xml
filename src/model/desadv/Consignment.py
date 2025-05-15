from src.model.self.desadv.PackingSequence import PackingSequence
from .base import DesadvBase

class Consignment(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)
        self.consignment = self.desadv.root.find(f'.//Consignment')
        self.packing_sequence = self.consignment.find('./PackingSequence') or self.consignment.find('./PACKING_SEQUENCE')
    packing_sequence: PackingSequence