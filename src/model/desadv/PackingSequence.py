from src.model.self.desadv.PackingReference import PackingReference
from src.model.self.desadv.Line import Line
from .base import DesadvBase

class PackingSequence(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)
        self.packingsequence = self.desadv.root.find(f'.//PackingSequence')
        self.packing_reference = self.packingsequence.find('./PackingReference') or self.packingsequence.find('./PACKING_REFERENCE')
        self.line = self.packingsequence.find('./Line') or self.packingsequence.find('./LINE')
    packing_reference: PackingReference
    line: Line